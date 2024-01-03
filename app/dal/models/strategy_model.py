from dataclasses import dataclass
from pdb import run

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
      max_draw_per = Column(Float)
      max_drawdown = Column(Float)
      max_dwawdown_duration = Column(Float)



      # strategy_performance (
      #                   id SERIAL PRIMARY KEY,
      #                   run_id INTEGER NOT NULL,
      #                   total_open NUMERIC NULL,
      #                   total_closed NUMERIC NULL,
      #                   total_won NUMERIC NULL,
      #                   total_lost NUMERIC NULL,
      #                   win_streak NUMERIC NULL,
      #                   lose_streak NUMERIC NULL,
      #                   pnl_net NUMERIC NULL,
      #                   strike_rate NUMERIC NULL,
      #                   sqn NUMERIC NULL,
      #                   total_compound_return NUMERIC NULL,
      #                   avg_return NUMERIC NULL,
      #                   annual_norm_return NUMERIC NULL,
      #                   max_draw_per NUMERIC NULL,
      #                   max_draw_val NUMERIC NULL,
      #                   max_draw_len NUMERIC NULL,
      #                   FOREIGN KEY (run_id) REFERENCES run_information(run_id)