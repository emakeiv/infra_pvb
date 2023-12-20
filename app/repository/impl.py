

from dal.models.exchanges_model import Exchange 
from dal.models.vendors_model import DataVendor
from dal.models.securities_model import (
      SecuritySymbol,
      SecurityDailyPrice,
      SecurityMinutelyPrice
)
from repository.entity import RepositoryEntity


'''
The repository classes acts as an intermediary between the 
application code and the database data mapping laters. Acting like an in-memory
collection of domain objects.It provides methods for 
retrieving, adding, updating, and deleting data entities in 
the database using the database session. The methods make use 
of the data model class, which is defined in the dal/models location, 
to interact with the underlying database tables.
'''

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
        super().__init__(SecuritySySecurityDailyPricembol, session)

class SecurityMinutelyPriceRepository(RepositoryEntity[SecurityMinutelyPrice]):
    def __init__(self, session):
        super().__init__(SecurityMinutelyPrice, session)

