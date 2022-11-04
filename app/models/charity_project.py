from sqlalchemy import Column, String, Text

from .abstract_model import AbstractModel


class CharityProject(AbstractModel):
    """Модель благотворительных проектов."""
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
