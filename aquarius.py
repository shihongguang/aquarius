from datetime import datetime

from server import TcpServer
from parse import parse_http
from response import json_response


class Aquarius(TcpServer):

    def __init__(self, **kwargs):
        super(Aquarius, self).__init__(**kwargs)
        self._route = {}

    def route(self, path):
        def inner(func):
            self._route[path] = func
        return inner

    def to_response(self, string, socket):
        self.http_parse(string,socket)
        request_dict = parse_http(string)

        try:
            msg = self._route[request_dict['path']](request_dict)
        except KeyError:
            print(request_dict['method'], request_dict['path'], '404 Not Found',
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            socket.send(json_response({'result': "Not Found"}))
        else:
            socket.send(msg)

    def http_parse(self, string_bytes, socket):
        list_res = string_bytes.decode('utf-8').splitlines()
