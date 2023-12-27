from datetime import datetime
from dataclasses import dataclass
from app.dal.models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Date,
    Index,
    Column,
    String,
    Integer,
    Numeric,
    TIMESTAMP,
    BigInteger,
    ForeignKey,
    ForeignKeyConstraint,
    PrimaryKeyConstraint
)

@dataclass
class SecuritySymbol(Base):
      __tablename__ = 'security_symbol'
      __metadata__ = Base.metadata
      
      id = Column(Integer, primary_key=True)
      exchange_id = Column(Integer, ForeignKey('exchange.id'))
      ticker = Column(String, index=True, nullable=False)
      instrument = Column(String, nullable=False)
      name = Column(String, nullable=False)
      sector = Column(String, nullable=False)
      currency = Column(String(64))
      created = Column(TIMESTAMP, nullable=False, default=datetime.now())
      updated = Column(TIMESTAMP, nullable=False, default=datetime.now()) 
      exchange = relationship("Exchange")

      def dict(self):
            return {
                  "security_id": self.id,
                  "ticker": self.ticker,
                  "instrument": self.instrument,
                  "name": self.name,
                  "sector": self.sector,
                  "exchange": self.exchange
        }

@dataclass
class SecurityDailyPrice(Base):
      __tablename__ = 'security_daily_price'
      __metadata__ = Base.metadata

      security_id = Column(Integer, ForeignKey('security_symbol.id'), nullable=False, index=True)
      data_vendor_id = Column(Integer, ForeignKey('data_vendor.id'), nullable=False)
      created = Column(TIMESTAMP, nullable=False, default=datetime.now())
      updated = Column(TIMESTAMP, nullable=False, default=datetime.now()) 
      date = Column(TIMESTAMP, index=True)
      open_price = Column(Numeric)
      high_price = Column(Numeric)
      low_price = Column(Numeric)
      close_price = Column(Numeric)
      volume = Column(BigInteger)
      
      data_vendor = relationship("DataVendor")
      security = relationship("SecuritySymbol")

      __table_args__ = (
            PrimaryKeyConstraint('security_id', 'date'),
      )

      def dict(self):
            return {
                  "security_id": self.id,
                  "date": self.date,
                  "open": self.open_price,
                  "high": self.high_price,
                  "low": self.low_price,
                  "close": self.close_price,
                  "volume": self.volume
        }
    

@dataclass
class SecurityMinutelyPrice(Base):
    __tablename__ = 'security_minute_price'
    __metadata__ = Base.metadata
    
    data_vendor_id = Column(Integer, ForeignKey('data_vendor.id'), nullable=False)
    security_id = Column(Integer, ForeignKey('security_symbol.id'), nullable=False, index=True)
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)
    date = Column(TIMESTAMP, index=True)
    open_price = Column(Numeric)
    high_price = Column(Numeric)
    low_price = Column(Numeric)
    close_price = Column(Numeric)
    volume = Column(BigInteger)
    data_vendor = relationship("DataVendor")
    security = relationship("SecuritySymbol")

    __table_args__ = (
        PrimaryKeyConstraint('security_id', 'date'),
    )

    def dict(self):
        return {
            "security_id": self.security_id,
            "date": self.date,
            "open": self.open_price,
            "high": self.high_price,
            "low": self.low_price,
            "close": self.close_price,
            "volume": self.volume
        }
