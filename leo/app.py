import uvloop
import asyncio
from server import ServerHttpProtocol
from response import json_response

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Aquarius(ServerHttpProtocol):

    def __init__(self):
        super(Aquarius, self).__init__()

        self._loop = asyncio.get_event_loop()
        self._route = {}

    def run(self, **kwargs):
        _server = self._loop.create_server(Aquarius, **kwargs)
        server = self._loop.run_until_complete(_server)

        try:
            self._loop.run_until_complete(server.wait_closed())
        except KeyboardInterrupt:
            print("server is closing")
        finally:
            server.close()

    def route(self, path):
        def _inner(view):
            self._route.update({path: view})
        return _inner

    def start_response(self):
        print(self._request)
        res = json_response({"name": "shihongguang"})
        self._transport.write(res)
        asyncio.sleep(10)
        self._transport.close()

app = Aquarius()
app.run(host='0.0.0.0', port=8001)
