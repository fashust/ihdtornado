# -*- coding: utf-8 -*- #
"""
    application handlers
"""
from tornado import gen
from tornado.web import RequestHandler

from application.models import User
from application.utils import dump_user_data


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class BaseRequestHandler(RequestHandler):
    """
        base request handler
    """
    @property
    def db(self):
        """
            get db session
        """
        return self.application.db

    @property
    def cache(self):
        """
            :return application redis connection
        """
        return self.application.cache

    def param(self, name, default=None, strip=True):
        """
            get request argument
        """
        return self.get_argument(name, default, strip)

    def get_current_user(self):
        """
            return current user
        """
        cookie = self.get_secure_cookie('user')
        if cookie:
            try:
                cookie = cookie.decode('utf-8')
            except UnicodeDecodeError as err:
                self.clear_cookie('user')
                return None
            user = self.db.query(User).filter(User.username==cookie).all()
            if user:
                return user[0]
        return None

    def _on_user_data(self, data):
        """
            user data callback
        """
        self.write({'status': True, 'data': data})
        self.finish()

    @gen.coroutine
    def dump_user_data(self, user):
        """
            dump all data related to user
        """
        yield gen.Task(
            dump_user_data, user, self.cache, self, self._on_user_data
        )