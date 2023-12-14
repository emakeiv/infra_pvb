
from services.oanda.fx_data_service import ForexDataService
from services.alpaca.stock_data_service import StockDataService

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
      fx_service = ForexDataService()
      a = fx_service.sayHi()
      print(a)