from server import TcpServer
from response import to_json_response


class Aquarius(TcpServer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url_func = {}

    def route(self, path):
        def inner(func):
            self.url_func[path] = func
        return inner

    def to_parse(self, string, socket):

        def string_splitlines(string):
            list_res = string.decode('utf-8').splitlines()
            return {'head': list_res[:-1],
                    'body': list_res[-1]}

        parse_request = string_splitlines(string)
        method, path, agreement = parse_request["head"][0].split()

        try:
            msg = self.url_func[path](parse_request)
        except KeyError:
            socket.send(to_json_response({"result": "Not Found"}))
        else:
            socket.send(msg)


if __name__ == '__main__':

    app = Aquarius(port=9000)

    @app.route("/")
    def test(request):
        return to_json_response({"name": "aquqrius"})

    @app.route("/favicon.ico")
    def test1(request):
        return to_json_response({"result": "Not Found"})

    app.start()
