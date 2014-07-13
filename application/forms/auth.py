# -*- coding: utf-8 -*- #
"""
    auth forms
"""
from wtforms import StringField, PasswordField, validators
from wtforms_tornado import Form


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'



class CreateUserForm(Form):
    """
        create user form
    """
    username = StringField('username', [validators.required()])
    email = StringField('email', [validators.Email(), validators.required()])
    password = PasswordField(
        'password',
        [validators.required(), validators.EqualTo(
            'password_confirm', message='Must match'
        )]
    )
    password_confirm = PasswordField(
        'password_confirm', [validators.required()]
    )