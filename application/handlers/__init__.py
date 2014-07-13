# -*- coding: utf-8 -*- #
"""
    application handlers
"""
from tornado.web import RequestHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class BaseRequestHandler(RequestHandler):
    """
        base request handler
    """
    @property
    def db(self):
        """
            get deb session
        """
        return self.application.db

    def param(self, name, default=None, strip=True):
        """
            get request argument
        """
        return self.get_argument(name, default, strip)

    def get_current_user(self):
        """
            return current user
        """
        # todo: implement
        return None