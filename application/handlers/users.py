# -*- coding: utf-8 -*- #
"""
    users views handlers
"""
from tornado.web import asynchronous

from application.handlers import BaseRequestHandler
from application.forms import CreateUserForm
from application.utils import check_email, create_user


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class UsersCreateViewHandler(BaseRequestHandler):
    """
        create user view handler
    """
    @asynchronous
    def post(self, *args, **kwargs):
        """
            post
        """
        self.create_form = CreateUserForm(self.request.arguments)
        if self.create_form.validate():
            check_email(
                self.async_callback(self._on_check_email),
                self.db, self.create_form.data['email']
            )
        return

    def _on_check_email(self, status, message):
        """
            on check email callback
        """
        if not status:
            self.write({'status': status, 'message': message})
            self.finish()
            return
        create_user(
            self.async_callback(self._on_create_user),
            self.db, self.create_form.data
        )

    def _on_create_user(self, user):
        """
            create new user
        """
        self.set_secure_cookie('user', user.username)
        self.write({'status': True})
        self.finish()