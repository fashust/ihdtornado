# -*- coding: utf-8 -*- #
"""
    tornado application
"""
from tornado.web import Application as TornadoApplication

from .settings import (
    TORNADO_SETTINGS, get_sessions, HANDLERS, REDIS_CONNECTION
)
from .models import Base as DBBase


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class Application(TornadoApplication):
    """
        tornado application
    """
    def __init__(self):
        """
            init
        """
        self.db = get_sessions(DBBase)
        self.cache = REDIS_CONNECTION
        super(Application, self).__init__(
            handlers=HANDLERS, **TORNADO_SETTINGS
        )