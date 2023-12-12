from datetime import datetime
from dataclasses import dataclass
from dal.models.base_model import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)


@dataclass
class Exchange(Base):
      __tablename__ = 'exchange'
      __metadata__ = Base.metadata
      id: int = Column(Integer, primary_key=True, unique=True, nullable=False)
      abbrev = Column(String, nullable=False)
      name: str = Column(String)
      currency = Column(String(64))
      created_date: datetime = Column(DateTime)
      updated_date: datetime = Column(DateTime)
     

