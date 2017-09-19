import functools
import logging
import asyncio 
import re

import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from server import HttpProtocol
from response import json_response


class Aquarius(HttpProtocol):

    _loop = asyncio.get_event_loop()
    _route_config = {}

    def __init__(self, name=None):
        super(Aquarius, self).__init__()
        self.name = name

    def run(self, **kwargs):
        try:
            self._loop.run_until_complete(self._loop.create_server(Aquarius, **kwargs))
            self._loop.run_forever()
        except KeyboardInterrupt:
            print("server is closing, byebye!")
            self._loop.stop()

    async def start_response(self, transport, request):
        try:
            res = await self._route_config.get(request.url.decode())(request)
            transport.write(res)
        except TypeError as e:
            print(request.url.decode())

    def route(self, path):
        def _inner(func):
            self._route_config.update({path: func})
        return _inner
