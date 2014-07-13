# -*- coding: utf-8 -*- #
"""
    users views handlers
"""
from application.handlers import BaseRequestHandler
from application.forms import CreateUserForm


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class UsersCreateViewHandler(BaseRequestHandler):
    """
        create user view handler
    """
    def post(self, *args, **kwargs):
        """
            post
        """
        create_form = CreateUserForm(self.request.arguments)
        print(create_form, self.request.arguments)
        print(self.param('username'), self.param('email'), self.param('password'))
        self.write({'status': True})