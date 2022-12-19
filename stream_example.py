import asyncio
import websockets
from saxo_openapi.contrib.ws import stream


async def Echo(ContextId, token):
    hdrs = {
        "Authorization": "Bearer {}".format(token),
    }
    URL = "wss://streaming.saxotrader.com/sim/openapi/streamingws/connect?" + \
          "contextId={ContextId}".format(ContextId=ContextId)
    async with websockets.connect(URL, extra_headers=hdrs) as websocket:
        async for raw_message in websocket:
            # get all messages from the raw message, nr. of messages varies
            print("----------------------------------")
            for message in stream.decode_ws_msg(raw_message):
                print(message)


if __name__ == "__main__":
    import sys

    with open("c://Users//LMDN//token24.txt") as I:
        token = I.read().strip()

    print(token)

    asyncio.get_event_loop().run_until_complete(Echo(ContextId=sys.argv[1],
                                                     token=token))