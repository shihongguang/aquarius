"""
server
"""

import socket
import select


class TcpServer(object):
    """Tcp Server"""

    def __init__(self, port=8000):
        self.port = port
        self.queue_size = 1000

    def start(self, port=8000):
        """server start"""
        self.port = port
        try:
            self.server_run()
        except KeyboardInterrupt:
            print("\r\nGood Bye!")

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
        """epoll"""
        return select.epoll()

    @property
    def max_bytes(self, num=1000):
        """rev max bytes"""
        return 1024 * num

    def server_run(self):
        """server run"""
        server_socket = self.server_socket
        server_f = server_socket.fileno()

        epoll = self.epoll
        epoll.register(server_f, select.EPOLLIN | select.EPOLLET)

        client_socket_fs = {}

        while True:
            epoll_list = epoll.poll()
            for _fd, event in epoll_list:
                if _fd == server_f:
                    socket_c, _ = server_socket.accept()
                    socket_c.setblocking(0)
                    client_socket_fs[socket_c.fileno()] = socket_c
                    epoll.register(socket_c.fileno(), select.EPOLLIN | select.EPOLLET)

                elif event == select.EPOLLIN:
                    bytes_request = client_socket_fs[_fd].recv(self.max_bytes)
                    if bytes_request:
                        self.to_response(bytes_request, client_socket_fs[_fd])
                    else:
                        epoll.unregister(_fd)
                        client_socket_fs[_fd].close()

    def to_response(self, string, socket_args):
        """parse string"""
        raise ValueError("not a function")
