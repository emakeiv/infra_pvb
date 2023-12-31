from dataclasses import dataclass

from app.dal.models.securities_model import SecurityDailyPrice

@dataclass
class CurrencyPrice(SecurityDailyPrice):
      pass