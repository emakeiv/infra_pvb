from datetime import datetime 

from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

from app.repository.registry import RepositoryRegistry 
from app.repository.impl import SecuritySymbolRepository
from app.dal.models.securities_model import SecuritySymbol

from app.env import settings

engine = create_engine(settings.main_db_url)
session = sessionmaker(bind=engine)()

repo_registry = RepositoryRegistry(session)
repo_registry.add('security_symbol_repo', SecuritySymbolRepository)

symbol_repo = repo_registry.get('security_symbol_repo')

records = [
  SecuritySymbol(
        ticker='AAPL', 
        instrument='Common Stock', 
        name='Apple Inc.', 
        sector='Technology', 
        created=datetime.now(), 
        updated=datetime.now()
  )
]
records = [r.__dict__ for r in records]
symbol_repo.bulk_insert(records)
session.commit()
