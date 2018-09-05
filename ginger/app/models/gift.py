from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('User.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)