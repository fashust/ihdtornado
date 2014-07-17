# -*- coding: utf-8 -*- #
"""
    utils
"""
from application.settings.db import get_sessions
from application.models import Base as DBBase
from .user_data import dump_user_data


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class AlchemySession(object):
    """
        create new sqlalchemy session
    """
    @staticmethod
    def get_db():
        """
            generate session object
        """
        return get_sessions(DBBase)