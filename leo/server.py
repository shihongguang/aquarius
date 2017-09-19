"""
storm
"""
import httptools
import asyncio


class ServerHttpProtocol(asyncio.Protocol):

    def __init__(self):
        self._transport = None
        self._parser = httptools.HttpRequestParser(self)
        self._request = {"headers": {}, "body": None}

    def connection_made(self, transport):
        self._transport = transport

    def data_received(self, data):
        try:
            self._parser.feed_data(data)
        except httptools.HttpParserError:
            pass

        self.start_response()

    def connection_lost(self, exc):
        self._transport.close()

    def on_url(self, url):
        self._request["url"] = url

    def on_header(self, name, value):
        self._request["headers"][name] = value

    def on_headers_complete(self):

        self._request["version"] = self._parser.get_http_version()
        self._request["method"] = self._parser.get_method()

    def on_body(self, body):
        self._request["body"] = body

    def on_message_complete(self):
        pass

    def start_response(self):
        pass
