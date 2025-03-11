import oandapyV20
import oandapyV20.endpoints.accounts as accounts

token = "883efad9fca0a50d48cf2cb3a91e8cf1-dbb3f49cb3d1e1507633f19794baa94d"
acc   = "101-012-22696074-001"

client = oandapyV20.API(access_token=token)
r = accounts.AccountInstruments(accountID=acc)
client.request(r)
print(r.response)