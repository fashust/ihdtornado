# -*- coding: utf-8 -*- #
"""
    urls handlers
"""
from application.handlers.index import IndexViewHandler
from application.handlers.users import UsersCreateViewHandler


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


HANDLERS = [
    (r'^/$', IndexViewHandler),
    (r'^/users/create/$', UsersCreateViewHandler)
]