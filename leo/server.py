"""
storm
"""
import httptools
import asyncio

from request import Request


class HttpProtocol(asyncio.Protocol):

    def __init__(self):
        self._transport = None
        self._parser = httptools.HttpRequestParser(self)
        self._request = Request()

    def connection_made(self, transport):
        self._transport = transport

    def data_received(self, data):
        try:
            self._parser.feed_data(data)
        except httptools.HttpParserError:
            pass

    def connection_lost(self, exc):
        self._transport.close()

    def on_url(self, url):
        self._request.url = url

    def on_header(self, name, value):
        self._request.headers[name] = value

    def on_headers_complete(self):

        self._request.version = self._parser.get_http_version()
        self._request.method = self._parser.get_method().decode()

    def on_body(self, body):
        self._request.body.append(body)

    def on_message_complete(self):
        if self._request.body:
            self._request.body = b"".join(self._request.body)

        self._loop.create_task(
            self.start_response(request=self._request, transport=self._transport)
        )

    async def start_response(self, transport, request):
        raise Exception("start_response not achieved")