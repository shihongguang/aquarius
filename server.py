import socket
import select


class TcpServer(object):

    def __init__(self,port=8000):
        self.port = port
        self.queue_size = 1000

    def start(self, port=8000):
        self.port = port
        self.server_run()

    @property
    def server_socket(self):
        """server socket"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setblocking(0)
        server_socket.bind(("", self.port))
        server_socket.listen(self.queue_size)
        return server_socket

    @property
    def epoll(self):
        return select.epoll()

    @property
    def max_bytes(self, num=1000):
        return 1024 * num

    def server_run(self):
        server_socket = self.server_socket
        server_f = server_socket.fileno()

        epoll = self.epoll
        epoll.register(server_f, select.EPOLLIN|select.EPOLLET)

        client_socket_fs = {}

        while True:
            epoll_list = epoll.poll()

            for f, e in epoll_list:
                if f == server_f:
                    s, _ = server_socket.accept()
                    s.setblocking(0)
                    client_socket_fs[s.fileno()] = s
                    epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)

                elif e == select.EPOLLIN:
                    bytes_request = client_socket_fs[f].recv(self.max_bytes)
                    if bytes_request:
                        self.to_parse(bytes_request, client_socket_fs[f])
                    else:
                        epoll.unregister(f)
                        client_socket_fs[f].close()

    def to_parse(self, string, socket):
        pass
