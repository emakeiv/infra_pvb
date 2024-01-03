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
class Exchange(Base):
    __tablename__ = 'exchange'
    __metadata__ = Base.metadata
    id = Column(Integer, primary_key=True)
    abbrev = Column(String, nullable=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=False)
    currency = Column(String(64))
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated = Column(TIMESTAMP, nullable=False, default=datetime.now())
     
    def dict(self):
        return {
            "id": self.id,
            "abbrev": self.abbrev,
            "code": self.code,
            "name": self.name,
            "currency": self.currency
        }
