from datetime import datetime 

from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

from app.repository.registry import RepositoryRegistry 
from app.repository.impl import DataVendorRepository
from app.dal.models.vendors_model import DataVendor
from app.env import settings

engine = create_engine(settings.main_db_url)
session = sessionmaker(bind=engine)()

repo_registry = RepositoryRegistry(session)
repo_registry.add('vendor_repo', DataVendorRepository)

vendor_repo = repo_registry.get('vendor_repo')

vendors = [
      {
            'name':'yahoo_finance',
            'url':'https://finance.yahoo.com/'
      },
      {
            'name':'google_finance',
            'url':'https://www.google.com/finance/?hl=en'
      },
      {       
            'name':'alpaca',
            'url':'https://alpaca.markets/'
      },
      {
            'name':'iex',
            'url':'https://www.iexexchange.io/'
      }, 
      {
            'name':'polygon',
            'url':'https://polygon.io/'
      },
      {
            'name':'oanda',
            'url':'https://www.oanda.com/us-en/'
      },
      {
            'name':'nasdaq_datalink',
            'url':'https://www.nasdaq.com/nasdaq-data-link'
      }
]

for i, vendor in enumerate(vendors):
      
      data_vendor = DataVendor(
            name = vendor['name'],
            website_url = vendor['url']
      )
      
      print(f"inserting {i} vendor: {data_vendor.name}")
      vendor_repo.add(data_vendor)

session.commit()
session.close()

