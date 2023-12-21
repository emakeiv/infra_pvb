from sqlalchemy import func

from dal.models.exchanges_model import Exchange 
from dal.models.vendors_model import DataVendor
from dal.models.securities_model import (
      SecuritySymbol,
      SecurityDailyPrice,
      SecurityMinutelyPrice
)
from repository.entity import RepositoryEntity

class ExchangeRepository(RepositoryEntity[Exchange]):
    def __init__(self, session):
        super().__init__(Exchange, session)

class DataVendorRepository(RepositoryEntity[DataVendor]):
    def __init__(self, session):
        super().__init__(DataVendor, session)

class SecuritySymbolRepository(RepositoryEntity[SecuritySymbol]):
    def __init__(self, session):
        super().__init__(SecuritySymbol, session)

class SecurityDailyPriceRepository(RepositoryEntity[SecurityDailyPrice]):
    def __init__(self, session):
        super().__init__(SecurityDailyPrice, session)
    
    def get_last_dates(self, tickers:list):
        query = self.session.query(
            SecuritySymbol.id.label('security_id'),
            SecuritySymbol.ticker,
            func.max(SecurityDailyPrice.date).label('last_date')
        ).outerjoin(
            SecurityDailyPrice, SecuritySymbol.id == SecurityDailyPrice.security_id
        ).filter(
            SecuritySymbol.ticker.in_(tickers)
        ).group_by(
            SecuritySymbol.id, SecuritySymbol.ticker
        )
        
        return query.all()

class SecurityMinutelyPriceRepository(RepositoryEntity[SecurityMinutelyPrice]):
    def __init__(self, session):
        super().__init__(SecurityMinutelyPrice, session)


