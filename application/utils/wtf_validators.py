# -*- coding: utf-8 -*- #
"""
    additional form validators
"""
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from wtforms import ValidationError

from application.models import User
from application.utils import AlchemySession


__author__ = 'fashust'
__email__ = 'fashust.nefor@gmail.com'


class UniqueEmail(AlchemySession):
    """
        check is email unique
    """
    def __init__(self, message=None):
        """
            init
        """
        if not message:
            message = 'Email уже используется'
        self.message = message

    def __call__(self, form, field):
        """
            call
        """
        db_session = self.get_db()
        result = db_session.query(User).filter(User.email==field.data).all()
        if result:
            db_session.close()
            raise ValidationError(self.message)
        db_session.close()


class UniqueUsername(AlchemySession):
    """
        check is username unique
    """
    def __init__(self, message=None):
        """
            init
        """
        if not message:
            message = 'Псевдоним уже используется'
        self.message = message

    def __call__(self, form, field):
        """
            call
        """
        db_session = self.get_db()
        result = db_session.query(User).filter(User.username==field.data).all()
        if result:
            db_session.close()
            raise ValidationError(self.message)
        db_session.close()


class PasswordMatch(AlchemySession):
    """
        password match to user stored password
    """
    def __init__(self, message=None):
        """
            init
        """
        if not message:
            message = 'Не верный пароль'
        self.message = message

    def __call__(self, form, field):
        """
            call
        """
        email = form.data.get('email', None)
        if email:
            db_session = self.get_db()
            try:
                result = db_session.query(User).filter(User.email==email).one()
            except (MultipleResultsFound, NoResultFound) as e:
                if isinstance(e, NoResultFound):
                    db_session.close()
                    # raise ValidationError('Пользователь не найден')
                    return
                elif isinstance(e, MultipleResultsFound):
                    db_session.close()
                    raise ValidationError('critical error')
            if result.password != field.data:
                db_session.close()
                raise ValidationError(self.message)
            form.user = result
            db_session.close()


class EmailExists(AlchemySession):
    """
        check is email exists
    """
    def __init__(self, message=None):
        """
            init
        """
        if not message:
            message = 'Пользователь не найден'
        self.message = message

    def __call__(self, form, field):
        """
            call
        """
        db_session = self.get_db()
        try:
            result = db_session.query(User).filter(
                User.email==field.data
            ).one()
        except (MultipleResultsFound, NoResultFound) as e:
            if isinstance(e, NoResultFound):
                db_session.close()
                raise ValidationError(self.message)
            elif isinstance(e, MultipleResultsFound):
                db_session.close()
                raise ValidationError('critical error')
        db_session.close()