# -*- coding: utf-8 -*- #
"""
    users views handlers
"""
from tornado import gen

from application.handlers import BaseRequestHandler
from application.forms import (CreateUserForm, AuthenticateUserForm)
from application.models import User


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
                self.check_email,
                create_form.data['email'],
            )
            status, message = result.args
            if not status:
                self.write({'status': status, 'message': message})
                return
            user = yield gen.Task(self.create_user, create_form.data.copy())
            self.set_secure_cookie('user', user.username)
            self.write({'status': True})
        else:
            self.write({
                'status': False,
                'message': 'form not valid',
                'errors': create_form.errors
            })

    def check_email(self, email, callback=None):
        """
            check is email used
        """
        result = self.db.query(User).filter(User.email==email).all()
        callback(
            True if not result else False,
            None if not result else 'email already used'
        )

    def create_user(self, form_data, callback=None):
        """
            create new user
        """
        # salt = uuid.uuid4().hex
        # password = hashlib.sha256(
        #     '{}{}'.format(form_data['password'], salt).encode('utf-8')
        # ).hexdigest()
        del(form_data['password_confirm'])
        # form_data['password'] = password
        user = User(**form_data)
        self.db.add(user)
        self.db.commit()
        callback(user)


class UsersAuthenticateViewHandler(BaseRequestHandler):
    """
        authenticate user view handler
    """
    def post(self, *args, **kwargs):
        """
            post
        """
        auth_form = AuthenticateUserForm(self.request.arguments)
        if auth_form.validate():
            pass
        self.write({
            'status': False,
            'message': 'form not valid',
            'errors': auth_form.errors
        })


class UsersLogoutViewHandler(BaseRequestHandler):
    """
        logout user handler
    """
    def get(self, *args, **kwargs):
        """
            get
        """
        self.clear_cookie('user')
        self.redirect('/')

    def post(self, *args, **kwargs):
        """
            post
        """
        return self.get(*args, **kwargs)