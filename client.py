import socket

from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange


class ServerDiscovery:
    def __init__(self):
        self.server_ip = None
        self.server_port = None

    def on_service_state_change(self, zeroconf, service_type, name, state_change):
        if state_change == ServiceStateChange.Added:
            if name == "MessageServer3._http._tcp.local.":
                info = zeroconf.get_service_info(service_type, name)
                if info:
                    self.server_ip = socket.inet_ntoa(info.addresses[0])
                    self.server_port = info.port

    def discover_server(self):
        zeroconf = Zeroconf()
        browser = ServiceBrowser(zeroconf, "_http._tcp.local.", handlers=[self.on_service_state_change])

        try:
            # Wait until the server is discovered
            while not self.server_ip:
                pass  # Keep waiting until server is discovered
        finally:
            zeroconf.close()

        return self.server_ip, self.server_port


class start_client():
    def __init__(self):
        self.discovery = ""
        self.client_socket = ""
        self.host, self.port = "",""
        self.current_move = ""
        self.opposition_move = ""
        self.side = ""
        self.connected = False

    def connect_to_server(self):
        self.discovery = ServerDiscovery()
        self.host, self.port = self.discovery.discover_server()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.connected = True
        print("connected")
        self.side = self.client_socket.recv(1024).decode("utf-8")
        print(self.side)
        if self.side == "blue":
            self.opposition_move = self.client_socket.recv(1024).decode("utf-8")
            if self.opposition_move[-3] != "-1]":
                if self.current_move:
                    self.client_socket.send(str(self.current_move).encode("utf-8"))
                    if self.current_move[-1] != -1:
                        self.opposition_move = self.client_socket.recv(1024).decode("utf-8")
                    self.current_move = ""
        elif self.side == "red":
            while True:
                if self.current_move:
                    self.client_socket.send(str(self.current_move).encode("utf-8"))
                    if self.current_move[-1] != -1:
                        self.opposition_move = self.client_socket.recv(1024).decode("utf-8")
                    self.current_move = ""
        self.client_socket.close()
