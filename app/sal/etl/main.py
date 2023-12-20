
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

      fx_data_service = ForexDataService()

      s3_data_service = S3DataService(
      "http://minio:9000",
      "minioadmin",
      "minioadmin",
      "sec-fx"
      )
      tickers = s3_data_service.read_excel("tickers.xlsx", sep=',', sheet_name="daily")
      print(tickers)

      # engine                       = create_engine('postgresql://pvb_main_user:pvb_main_user@localhost/pvb_data')
      # session                      = sessionmaker(bind=engine)
      
      # repository_registry = RepositoryRegistry(session)
      # repository_registry.add('security_symbol_repo', SecuritySymbolRepository)
      # repository_registry.add('security_daily_price_repo',SecurityDailyPriceRepository)
      # repository_registry.add('security_minutely_price_repo',SecurityMinutelyPriceRepository)
      # repository_registry.add('data_vendor_repo',DataVendorRepository)
      # repository_registry.add('exchange_repo',ExchangeRepository)
    

