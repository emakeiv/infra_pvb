from datetime import datetime
from dataclasses import dataclass
from dal.models.base_model import Base

from sqlalchemy import (
    Date,
    Column,
    String,
    Integer,
    Numeric,
    Boolean,
    DateTime,
    BigInteger,
    ForeignKey,
    ForeignKeyConstraint,
    PrimaryKeyConstraint
)


@dataclass
class SecuritySymbol(Base):
      __tablename__ = 'security'
      __metadata__ = Base.metadata

      id: int = Column(Integer, primary_key=True, unique=True, nullable=False)
      created_date: datetime = Column(DateTime)
      updated_date: datetime = Column(DateTime)
      exchange_id: str = Column(String)
      ticker: str = Column(String)
      name: str = Column(String)
      sector: str = Column(String)
      currency: str = Column(String(64))
      exchange: str = Column(String)

@dataclass
class SecurityDailyPrice(Base):
      __tablename__ = 'security_daily_price'
      __metadata__ = Base.metadata

      security_id: int = Column(Integer, ForeignKey('security.id'), nullable=False)
      created_date: datetime = Column(DateTime)
      updated_date: datetime = Column(DateTime)
      date: datetime = Column(DateTime(timezone=False), nullable=False)
      open: float = Column(Numeric)
      high: float = Column(Numeric)
      low: float = Column(Numeric)
      close: float = Column(Numeric)
      volume: int = Column(BigInteger)

      __table_args__ = (
            PrimaryKeyConstraint('security_id', 'date'),
      )
    

@dataclass
class SecurityMinutelyPrice(Base):
      __tablename__ = 'security_minute_price'
      __metadata__ = Base.metadata

      security_id: int = Column(Integer, ForeignKey('security.id'), nullable=False)
      created_date: datetime = Column(DateTime)
      updated_date: datetime = Column(DateTime)
      date: datetime = Column(DateTime(timezone=False), nullable=False)
      open: float = Column(Numeric)
      high: float = Column(Numeric)
      low: float = Column(Numeric)
      close: float = Column(Numeric)
      volume: int = Column(BigInteger)

      __table_args__ = (
            PrimaryKeyConstraint('security_id', 'date'),
      )

