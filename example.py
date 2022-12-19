from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
import saxo_openapi.endpoints.portfolio as pf
import saxo_openapi.endpoints.referencedata as rd
from saxo_openapi.contrib.session import account_info
from saxo_openapi.definitions.orders import AssetType as AT
import json
import juputil
from pprint import pprint
from os import path

home_directory = path.expanduser( '~' )
token_directory = home_directory + '\\token24.txt'

with open(token_directory) as f:
    token24 = f.readlines()

token24 = token24[0]

client = API(access_token=token24)
ai = account_info(client)



# lets make a diagnostics request, it should return '' with a state 200
r = rs.diagnostics.Get()
print("request is: ", r)
rv = client.request(r)
assert rv is None and r.status_code == 200
print('diagnostics passed')

# request available rootservices-features
r = rs.features.Availability()
rv = client.request(r)
print("request is: ", r)
print("response: ")
pprint(rv, indent=2)
print(r.status_code)

# request client details
r = pf.clients.ClientDetailsMe()
rv = client.request(r)
pprint(rv)

# params from above
params = {
    'ClientKey': rv['ClientKey']
}

# request the balances
r = pf.balances.AccountBalances(params=params)
rv = client.request(r)
pprint(rv)

# Look up Vestas
r = rd.instruments.Instruments(params = {'AccountKey': ai.AccountKey,
                                         'KeyWords': 'Vestas',
                                         'AssetTypes': AT.Stock,
                                         'ExchangeIds': 'CSE'})
print(json.dumps(client.request(r), indent=2))

