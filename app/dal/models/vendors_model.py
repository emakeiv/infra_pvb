from datetime import datetime
from dataclasses import dataclass
from app.dal.models.base_model import Base

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
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated = Column(TIMESTAMP, nullable=False, default=datetime.now())

    def dict(self):
        return {
            "security_id": self.id,
            "name": self.name,
            "website_url": self.website_url
        }