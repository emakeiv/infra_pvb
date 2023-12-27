from datetime import datetime 

from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

from app.repository.registry import RepositoryRegistry 
from app.repository.impl import SecuritySymbolRepository
from app.dal.models.exchanges_model import Exchange

from app.env import settings

import alpaca_trade_api as tradeapi

engine = create_engine(settings.main_db_url)
session = sessionmaker(bind=engine)()

api = tradeapi.REST(
      settings.alpaca_api_key, 
      settings.alpaca_sec_key,
      settings.alpaca_base_url
      )
assets = api.list_assets()

exchanges = set()
for asset in assets:
    if asset.exchange not in exchanges:
        exchange = Exchange(
            abbrev=asset.exchange,
            name=asset.exchange, 
            currency='USD',
            created=datetime.now(),
            updated=datetime.now()
        )
        exchanges.add(asset.exchange)
        print(f"Inserting exchange {exchange.abbrev}")
        session.add(exchange)

session.commit()