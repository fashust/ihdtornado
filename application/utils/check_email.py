# -*- coding: utf-8 -*- #
"""
    check email
"""
from application.models import User


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


def check_email(callback, db_session, email):
    """
        check is email used
    """
    result = db_session.query(User).filter(User.email==email).all()
    callback(
        True if not result else False,
        None if not result else 'email already used'
    )
    return