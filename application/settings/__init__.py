# -*- coding: utf-8 -*- #
"""
    application settings
"""
import os
from application import uimodules


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


DEBUG = True
XSRF_COOKIE = True
COOKIE_SECRET = 'CR7Uw/XZTgGSDkPIaHylRc7ec6rWDERBm9alavT8SIQ='
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


TORNADO_SETTINGS = {
    'debug': DEBUG,
    'template_path': os.path.join(PROJECT_ROOT, 'templates'),
    'static_path': os.path.join(PROJECT_ROOT, 'static'),
    'xsrf_cookies': XSRF_COOKIE,
    'cookie_secret': COOKIE_SECRET,
    'ui_modules': uimodules
}


from .db import get_sessions
from .urls import HANDLERS
from .redis_conf import REDIS_CONNECTION