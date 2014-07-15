# -*- coding: utf-8 -*- #
"""
    users views handlers
"""
from tornado import gen

from application.handlers import BaseRequestHandler
from application.forms import CreateUserForm
from application.utils import check_email, create_user


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class UsersCreateViewHandler(BaseRequestHandler):
    """
        create user view handler
    """
    @gen.coroutine
    def post(self, *args, **kwargs):
        """
            post
        """
        create_form = CreateUserForm(self.request.arguments)
        if create_form.validate():
            result = yield gen.Task(
                check_email,
                self.db,
                create_form.data['email'],
            )
            status, message = result.args
            if not status:
                self.write({'status': status, 'message': message})
                return
            user = yield gen.Task(create_user, self.db, create_form.data)
            self.set_secure_cookie('user', user.username)
            self.write({'status': True})
        else:
            self.write({'status': False, 'message': 'form not valid'})