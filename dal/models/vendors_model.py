from datetime import datetime
from dataclasses import dataclass
from dal.models.base_model import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    TIMESTAMP
)

@dataclass
class DataVendor(Base):
    __tablename__ = 'data_vendor'
    __metadata__ = Base.metadata
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    website_url = Column(String(255))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

