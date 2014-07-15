# -*- coding: utf-8 -*- #
"""
    create user
"""
import hashlib
import uuid
from application.models import User


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


def create_user(db_session, data, callback=None):
    """
        create new user
    """
    salt = uuid.uuid4().hex
    password = hashlib.sha256(
        '{}{}'.format(data['password'], salt).encode('utf-8')
    ).hexdigest()
    del(data['password_confirm'])
    data['password'] = password
    user = User(**data)
    db_session.add(user)
    db_session.commit()
    callback(user)