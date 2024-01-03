import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.dal.models.securities_model import SecurityDailyPrice

from sal.services.oanda.data_service import OandaDataService
from sal.services.yahoo_finance.data_service import YahooFinanceDataService
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

def extract():
      pass 

def transform():
      pass

def load(data, repo, vendor_id, security_id):
      records = list()
      check_duplicates = set()
      for time, row in data.iterrows():
            record_identifier = (security_id, time)
            if record_identifier in check_duplicates:
                  print(f"skipping duplicate record with security_id:{security_id}, date:{time}")
                  continue

            existing_record = repo.get(security_id=security_id, date=time)
            if existing_record is not None:
                  print(f"skipping existing record with security_id:{security_id}, date:{time}")
                  continue

            check_duplicates.add(record_identifier)
            _record = SecurityDailyPrice(
                  security_id = security_id,
                  data_vendor_id= vendor_id,
                  date = time,
                  open_price = row.open,
                  high_price = row.high,
                  low_price = row.low,
                  close_price = row.close,
                  volume = row.volume
            )
            records.append(_record.dict())
      if records:
            repo.bulk_insert(records)
      

def main():
      initial_start_date = datetime.datetime(2010,12,30)
      market_data_service = OandaDataService(
            access_token = settings.oanda_api_key,
            account_id= settings.oanda_acc_id
      )

      s3_data_service = S3DataService(
      "http://minio:9000",
      settings.aws_secret_access_key,
      settings.aws_access_key_id,
      "sec-fx"
      )
      tickers = s3_data_service.read_excel("tickers.xlsx", sheet_name="daily")
      
      engine                       = create_engine(settings.main_db_url)
      session                      = sessionmaker(bind=engine)()
      
      repository_registry = RepositoryRegistry(session)
      repository_registry.add('exchange_repo', ExchangeRepository)
      repository_registry.add('data_vendor_repo', DataVendorRepository)
      repository_registry.add('security_daily_price_repo', SecurityDailyPriceRepository)
      repository_registry.add('security_minutely_price_repo', SecurityMinutelyPriceRepository)
     
      
      if not tickers.empty:     
            daily_price_repo = repository_registry.get('security_daily_price_repo')
            data_vendor_repo = repository_registry.get('data_vendor_repo')
            vendor_id = data_vendor_repo.get(name="oanda").id
            last_day_prices = daily_price_repo.get_last_dates(tickers.symbols.tolist())

            for security_id, symbol, last_date in last_day_prices:
                  print(f'vendor id: {vendor_id}, security id: {security_id}, symbol: {symbol}, last date: {last_date}')
                  last_date = last_date + datetime.timedelta(days=1) if last_date else initial_start_date
                  try:
                        data = market_data_service.fetch_data(symbol, start_date=last_date, granularity='D')
                        print(f'fetching {symbol} market data from {last_date} to {datetime.datetime.now()}')
                        loaded_data = load(data, daily_price_repo, vendor_id=vendor_id, security_id=security_id)
                        print(f"{symbol} market data is loaded into database")

                  except Exception as e:
                        print(f"Error processing {symbol}: {e}")


