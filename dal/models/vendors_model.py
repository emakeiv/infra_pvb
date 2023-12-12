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
class DataVendors(Base):
      __tablename__ = 'data_vendor'
      __metadata__ = Base.metadata
      id: int = Column(Integer, primary_key=True, unique=True, nullable=False)
      name: str = Column(String)
      website_url: str = Column(String(64))
      created_date: datetime = Column(DateTime)
      updated_date: datetime = Column(DateTime)

