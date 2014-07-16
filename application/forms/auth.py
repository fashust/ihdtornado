# -*- coding: utf-8 -*- #
"""
    auth forms
"""
from wtforms import StringField, PasswordField, validators
from wtforms_tornado import Form

from application.utils.wtf_validators import (
    UniqueEmail, UniqueUsername,  EmailExists, PasswordMatch
)


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'



class CreateUserForm(Form):
    """
        create user form
    """
    username = StringField('username', [
        validators.required(),
        UniqueUsername()
    ])
    email = StringField('email', [
        validators.Email(), validators.required(), UniqueEmail()
    ])
    password = PasswordField(
        'password', [
            validators.required(), validators.EqualTo(
                'password_confirm', message='Пароли не совпадают'
            )
        ]
    )
    password_confirm = PasswordField(
        'password_confirm', [
            validators.required(), validators.EqualTo(
                'password', message='Пароли не совпадают'
            )
        ]
    )


class AuthenticateUserForm(Form):
    """
        authenticate user form
    """
    email = StringField(
        'email',
        [validators.Email(), validators.required(), EmailExists()]
    )
    password = PasswordField(
        'password',
        [validators.required(), PasswordMatch()]
    )