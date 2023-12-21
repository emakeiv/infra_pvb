
from sal.services.oanda.data_service import ForexDataService
from sal.services.boto.data_service import S3DataService
from repository.registry import RepositoryRegistry
from repository.impl import (
      SecuritySymbolRepository,
      SecurityDailyPriceRepository,
      SecurityMinutelyPriceRepository,
      DataVendorRepository,
      ExchangeRepository
)

from app.env import settings

def fetch_tickers():
      pass

def fetch_vendor_id():
      pass

def extract():
      pass 

def transform():
      pass

def load():
      pass 

def main():

      fx_data_service = ForexDataService(settings.oanda_api_key,settings.oanda_acc_id)

      s3_data_service = S3DataService(
      "http://minio:9000",
      "minioadmin",
      "minioadmin",
      "sec-fx"
      )
      tickers = s3_data_service.read_excel("tickers.xlsx", sheet_name="daily").tolist()
      

      engine                       = create_engine(settings.main_db_url)
      session                      = sessionmaker(bind=engine)()
      
      repository_registry = RepositoryRegistry(session)
      repository_registry.add('security_symbol_repo', SecuritySymbolRepository)
      repository_registry.add('security_daily_price_repo',SecurityDailyPriceRepository)
      repository_registry.add('security_minutely_price_repo',SecurityMinutelyPriceRepository)
      repository_registry.add('data_vendor_repo',DataVendorRepository)
      repository_registry.add('exchange_repo',ExchangeRepository)

      daily_price_repo = repository_registry.get('security_daily_price_repo')
      # last_dates_for_tickers = daily_price_repo.get_last_dates(tickers)
      
      instrument, granularity, _from = "EUR_USD", "M15", "2023-12-20T00:00:00Z"

      data = fx_data_service.fetch_historical_data(instrument=instrument, start_date=_from, granularity=granularity)
      print(data)


