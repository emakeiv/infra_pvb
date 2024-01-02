from datetime import datetime 

from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

from app.repository.registry import RepositoryRegistry 
from app.repository.impl import SecuritySymbolRepository, ExchangeRepository
from app.dal.models.exchanges_model import Exchange
from app.dal.models.securities_model import SecuritySymbol

from app.env import settings

import pandas as pd
import alpaca_trade_api as tradeapi

engine = create_engine(settings.main_db_url)
session = sessionmaker(bind=engine)()

api = tradeapi.REST(
      settings.alpaca_api_key, 
      settings.alpaca_sec_key,
      settings.alpaca_base_url
      )

repo_registry = RepositoryRegistry(session)
repo_registry.add('security_symbol_repo', SecuritySymbolRepository)
repo_registry.add('exchange_repo', ExchangeRepository)

symbol_repo = repo_registry.get('security_symbol_repo')
exchange_repo = repo_registry.get('exchange_repo')

tickers_df = pd.read_excel('data/oanda_fx_tickers.xlsx', sheet_name='daily')

for i, symbol in enumerate(tickers_df.symbols):

      security_symbol = SecuritySymbol(
            exchange_id=9,
            ticker=symbol,
            instrument='forex',
            name = ' ',
            sector = ' ',
            currency = ' ',
            created=datetime.now(),
            updated=datetime.now()
      )
      print(f"inserting {i} symbol: {symbol}")
      symbol_repo.add(security_symbol)

session.commit()
session.close()

# assets = api.list_assets()

# for i, asset in enumerate(assets):
#       if asset.tradable:
          
#             exchange = exchange_repo.get(abbrev=asset.exchange)
#             #print(f"exchange id: {exchange.id}")
#             security_symbol = SecuritySymbol(
#                   exchange_id=exchange.id,
#                   ticker=asset.symbol,
#                   instrument=asset.__getattr__('class'),
#                   name=asset.name, 
#                   sector='',
#                   currency="USD",
#                   created=datetime.now(),
#                   updated=datetime.now()
#             )
#             print(f"inserting {i} symbol: {asset.symbol}")
#             symbol_repo.add(security_symbol)

# session.commit()
# session.close()