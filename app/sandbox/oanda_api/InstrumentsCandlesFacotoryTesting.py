import json
from oandapyV20 import API
from oandapyV20.contrib.factories import InstrumentsCandlesFactory

token = "883efad9fca0a50d48cf2cb3a91e8cf1-dbb3f49cb3d1e1507633f19794baa94d"

client = API(access_token=token)
instrument, granularity = "EUR_USD", "M15"
_from = "2023-12-14T00:00:00Z"
params = {
      "from": _from,
      "granularity": granularity,
      "count": 2500,
}
with open("{}.{}".format(instrument, granularity), "w") as outfile:
      # The factory returns a generator generating consecutive
      # requests to retrieve full history from date 'from' till 'to'
      for r in InstrumentsCandlesFactory(instrument=instrument, params=params):
            client.request(r)
            print(r.response)
            #outfile.write(json.dumps(r.response.get('candles'), indent=2))