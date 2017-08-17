from datetime import datetime

from server import TcpServer
from parse import parse_http
from response import json_response


class Aquarius(TcpServer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url_route = {}

    def route(self, path):
        def inner(func):
            self.url_route[path] = func
        return inner

    def to_parse(self, string, socket):
        request_dict = parse_http(string)

        try:
            msg = self.url_route[request_dict['path']](request_dict)
        except KeyError:
            print(request_dict['method'], request_dict['path'], '404 Not Found', 
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            socket.send(json_response({'result': "Not Found"}))
        else:
            socket.send(msg)


if __name__ == '__main__':

    app = Aquarius()

    @app.route("/")
    def test(request):
        return json_response({"name": "aquqrius"})

    @app.route("/favicon.ico")
    def test1(request):
        return json_response({"result": "Not Found"})

    app.start(port=8888)
