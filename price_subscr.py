from saxo_openapi import API
import saxo_openapi.endpoints.trading as tr
import saxo_openapi.endpoints.referencedata as rd
import saxo_openapi.contrib.session as session
import json

def subscribe_for_prices(client, ContextId, instruments):
    """fetch instrument data by the name of the instrument and extract the Uic (Identifier)
    and use that to subscribe for prices.
    Use the name of the instrument as reference.
    """
    _ai = session.account_info(client=client)

    # body template for price subscription
    body = {
       "Arguments": {
           "Uic": "",
           "AssetType": "FxSpot"
       },
       "ContextId": "",
       "ReferenceId": ""
    }
    body.update({'ContextId': ContextId})

    for instrument in instruments:
        params = {'AccountKey': _ai.AccountKey,
                  'AssetTypes': 'FxSpot',
                  'Keywords': instrument
                 }
        # create the request to fetch Instrument info
        r = rd.instruments.Instruments(params=params)
        rv = client.request(r)
        if len(rv['Data']) == 1:
            body['Arguments'].update({'Uic': rv['Data'][0]['Identifier']})
            body.update({"ReferenceId": instrument})
            # print("Prepping: ")
            # print(json.dumps(body, indent=2))
            # create the request to fetch Instrument info
            r = tr.prices.CreatePriceSubscription(data=body)
            client.request(r)

            status = "succesful" if r.status_code == r.expected_status else "failed"
            print("Subscription for instrument: {} {}".format(instrument, status))

        else:
            print("Got multiple instruments for {}, can't choose...skip".format(instrument))


if __name__ == "__main__":

    import sys
    with open("c://Users//LMDN//token24.txt") as I:
        token = I.read().strip()
   
    client = API(access_token=token)
    ContextId = sys.argv[1]
    subscribe_for_prices(client, ContextId, sys.argv[2:])
    print("check the stream for data ...")