from dataclasses import dataclass
from pdb import run
from re import T

from numpy import record, size

from dal.models.base_model import Base
from sqlalchemy import (
      Column, 
      Integer, 
      String, 
      DateTime, 
      Float,
      Boolean, 
      ForeignKey
)

@dataclass
class RunInformation(Base):
      __tablename__ = 'run_information'
      __metadata__ = Base.metadata 
      id = Column(Integer, primary_key=True)
      type = Column(String, nullable=False)
      recorded_time = Column(DateTime, nullable=False)
      start_time = Column(DateTime, nullable=False)
      end_time = Column(DateTime, nullable=True)
      strategy = Column(String, nullable=False)
      tickers = Column(String, nullable=False)
      indicators = Column(String, nullable=True)
      frequency = Column(String, nullable=False)
      account = Column(String, nullable=False)
      log_file = Column(String, nullable=True)

@dataclass
class StrategyPerformance(Base):
      __tablename__ ='strategy_performance'
      __metadata__ = Base.metadata  

      id = Column(Integer, primary_key=True)
      run_id = Column(Integer, ForeignKey('run_information.id'))
      total_open = Column(Float)
      total_closed = Column(Float)
      total_won = Column(Float)
      total_lost = Column(Float)
      win_streak = Column(Float)
      lose_streak = Column(Float)
      pnl_net = Column(Float)
      strike_rate = Column(Float)
      sqn = Column(Float)
      total_compound_return = Column(Float)
      avg_return = Column(Float)
      annual_norm_return = Column(Float)
      max_draw_percentage = Column(Float)
      max_drawdown = Column(Float)
      max_dwawdown_duration = Column(Float)


@dataclass
class PositionPerformance(Base):
      __tablename__ ='position_performance'
      __metadata__ = Base.metadata
      id = Column(Integer, primary_key=True)
      run_id = Column(Integer, ForeignKey('run_information.id'))
      recorded_time = Column(DateTime, nullable=False)
      strategy = Column(String, nullable=False)
      ref = Column(Integer, nullable=False)
      direction = Column(String, nullable=False)
      ticker = Column(String, nullable=False)
      datein = Column(DateTime, nullable=False)
      pricein = Column(Float, nullable=False)
      dateout = Column(DateTime, nullable=False)
      priceout = Column(Float, nullable=False)
      change_percentage = Column(Float, nullable=False)
      pnl = Column(Float, nullable=False)
      pnl_percentage = Column(Float, nullable=False)
      size = Column(Float, nullable=False)
      value = Column(Float, nullable=False)
      cumpln = Column(Float, nullable=False)
      nbars = Column(Float, nullable=False)
      pnl_per_bar = Column(Float, nullable=False)
      mfe_percentage = Column(Float)
      mae_percentage = Column(Float)

@dataclass
class Positions(Base):
      __tablename__ = 'positions'
      __metadata__ = Base.metadata
      run_id = Column(Integer, ForeignKey('run_information.id'))
      recorded_time = Column(DateTime, nullable=False)
      strategy = Column(String, nullable=False)
      transaction_date = Column(DateTime, nullable=False)
      size = Column(Float, nullable=False)
      price = Column(Float, nullable=False)
      sid = Column(Integer, nullable=False)
      ticker = Column(String, nullable=False)
      value = Column(Float, nullable=False)