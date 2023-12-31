from datetime import datetime 

from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

from app.repository.registry import RepositoryRegistry 
from app.repository.impl import (
      SecuritySymbolRepository,
      SecurityDailyPriceRepository,
      SecurityMinutelyPriceRepository
)
from app.dal.models.securities_model import (
      SecuritySymbol,
      SecurityDailyPrice,
      SecurityMinutelyPrice
)

from app.env import settings
engine = create_engine(settings.main_db_url)
session = sessionmaker(bind=engine)()
