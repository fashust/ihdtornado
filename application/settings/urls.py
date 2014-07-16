# -*- coding: utf-8 -*- #
"""
    urls handlers
"""
from application.handlers.index import IndexViewHandler
from application.handlers.users import (
    UsersCreateViewHandler, UsersLogoutViewHandler,
    UsersAuthenticateViewHandler
)


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


HANDLERS = [
    (r'^/$', IndexViewHandler),
    (r'^/users/create/$', UsersCreateViewHandler),
    (r'^/users/logout/$', UsersLogoutViewHandler),
    (r'^/users/auth/$', UsersAuthenticateViewHandler)
]