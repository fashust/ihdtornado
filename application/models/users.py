# -*- coding: utf-8 -*- #
"""
    users models
"""
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_utils import PasswordType, URLType

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
    password = Column(PasswordType(
        schemes=['pbkdf2_sha512',]
    ), nullable=False, name='password')
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
    avatar = Column(URLType, nullable=True, default=None, name='avatar')

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns if column.name != 'password'
        }

    @property
    def flats(self):
        """
            get all flats belong to user
        """
        return []

    @property
    def display_name(self):
        """
            pretty user name
        """
        return ('{} {}'.format(self.first_name, self.first_name)
                if self.first_name and self.last_name else self.username)