# -*- coding: utf-8 -*- #
"""
    database settings
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


DB_STRING = 'postgresql+psycopg2://postgres:idit06m@localhost/ihdtornado'


def get_sessions(base):
    """
        :param base - sqlalchemy Base class
        :return sqlalchemy scoped session
    """
    if base:
        engine = create_engine(DB_STRING)
        base.metadata.create_all(bind=engine)
        return scoped_session(sessionmaker(bind=engine))

