import socket
from zeroconf import Zeroconf, ServiceInfo


class server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.local_IP = socket.gethostbyname(self.host)
        self.port = 5000
        self.server_socket.bind(("0.0.0.0", self.port))
        self.server_socket.listen(5)
        self.current_move = ""
        self.opposition_move = ""
        self.connected = False
        self.side = ""

    def create_mDNS(self):
        zeroconf = Zeroconf()
        service_info = ServiceInfo(
            "_http._tcp.local.",
            "MessageServer2._http._tcp.local.",
            addresses=[socket.inet_aton(self.local_IP)],
            port=5000,
            properties={},
            server=f"{self.host}.local"

        )
        zeroconf.register_service(service_info)

        client_socket, client_address = self.server_socket.accept()
        print("connected")
        self.connected = True
        client_socket.send("blue".encode("utf-8")) if self.side == "red" else client_socket.send("red".encode("utf-8"))

        if self.side == "red":
            while True:
                if self.current_move:
                    client_socket.send(str(self.current_move).encode("utf-8"))
                    if self.current_move[-1] != -1:
                        self.opposition_move = client_socket.recv(1024).decode("utf-8")
                    self.current_move = ""
        elif self.side == "blue":
            while True:
                self.opposition_move = client_socket.recv(1024).decode("utf-8")
                if self.opposition_move[-3] != "-1]":
                    if self.current_move:
                        client_socket.send(str(self.current_move).encode("utf-8"))
                        if self.current_move[-1] != -1:
                            self.opposition_move = client_socket.recv(1024).decode("utf-8")
                        self.current_move = ""
        zeroconf.unregister_service(service_info)
        zeroconf.close()
        client_socket.close()
        self.server_socket.close()
