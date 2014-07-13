# -*- coding: utf-8 -*- #
"""
    database models
"""
from sqlalchemy.ext.declarative import declarative_base


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


Base = declarative_base()


from .users import User