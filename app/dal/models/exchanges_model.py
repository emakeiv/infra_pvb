from dataclasses import dataclass
from dal.models.base_model import Base

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
    abbrev = Column(String, nullable=False)
    name = Column(String, nullable=False)
    currency = Column(String(64))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)
     

