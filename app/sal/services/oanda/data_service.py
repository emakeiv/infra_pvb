import oandapyV20
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments

from oandapyV20 import API
from oandapyV20.contrib.factories import InstrumentsCandlesFactory


class ForexDataService():

    def __init__(self, access_token, acc_id, environment='practice', headers=None, request_params=None):
            
            self.acc_id = acc_id
            self.client = API(access_token=access_token, environment=environment)
    def health_check(self):
            return 'Hi'

    def fetch_historical_data(self, instrument, start_date, end_date, granularity='D'):
        """
        Fetch historical data for a given financial instrument from OANDA API.
        Args:
            instrument (str): The name of the financial instrument.
            start_date (str): The start date for the data in YYYY-MM-DD format.
            end_date (str): The end date for the data in YYYY-MM-DD format.
            granularity (str): The granularity of the data (e.g., 'D' for daily).
        Returns:
            pd.DataFrame: A DataFrame containing the historical data.
        """

        params = {
            "from": start_date,
            "granularity": granularity,
            "count": 2500,  # Maximum number of data points
        }

        #   params = {
        #     "from": start_date,
        #     "to": end_date,
        #     "granularity": granularity,
        #     "count": 2500,  # Maximum number of data points
        # }

        full_data = []
        for response in InstrumentsCandlesFactory(instrument=instrument, params=params):
            self.client.request(response)
            candles = response.response.get('candles')
            if candles:
                for candle in candles:
                    candle_data = [
                        candle['time'], candle['volume'],
                        candle['mid']['o'], candle['mid']['h'],
                        candle['mid']['l'], candle['mid']['c']
                    ]
                    full_data.append(candle_data)

        df = pd.DataFrame(full_data, columns=['time', 'volume', 'open', 'high', 'low', 'close'])
        df['time'] = pd.to_datetime(df['time'])
        df.set_index('time', inplace=True)
        return df