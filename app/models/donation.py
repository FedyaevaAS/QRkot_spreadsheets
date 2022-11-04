from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract_model import AbstractModel


class Donation(AbstractModel):
    """Модель пожертвований пользователей."""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
