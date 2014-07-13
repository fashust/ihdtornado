# -*- coding: utf-8 -*- #
"""
    users models
"""
import datetime

from sqlalchemy import Column, Integer, String, DateTime

from application.models import Base

__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class User(Base):
    """
        users model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, name='id')
    username = Column(String(60), nullable=False, name='username')
    password = Column(String(80), nullable=False, name='password')
    first_name = Column(
        String(60), nullable=True, name='first_name', default=''
    )
    last_name = Column(
        String(60), nullable=True, name='last_name', default=''
    )
    date_joined = Column(DateTime(
        timezone=False), default=datetime.datetime.now, name='date_joined'
    )
    email = Column(String(60), nullable=True, default='', name='email')