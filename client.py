import socket

from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange


class ServerDiscovery:
    def __init__(self):
        self.server_ip = None
        self.server_port = None

    def on_service_state_change(self, zeroconf, service_type, name, state_change):
        if state_change == ServiceStateChange.Added:
            print("service discovered: ",name)
            if name == "MessageServer1._http._tcp.local.":
                info = zeroconf.get_service_info(service_type, name)
                if info:
                    self.server_ip = socket.inet_ntoa(info.addresses[0])
                    self.server_port = info.port
                    print(f"Discovered server: {self.server_ip}:{self.server_port}")

    def discover_server(self):
        zeroconf = Zeroconf()
        browser = ServiceBrowser(zeroconf, "_http._tcp.local.", handlers=[self.on_service_state_change])

        print("Searching for the server...")
        try:
            # Wait until the server is discovered
            while not self.server_ip:
                pass  # Keep waiting until server is discovered
        finally:
            zeroconf.close()

        return self.server_ip, self.server_port


discovery = ServerDiscovery()
host, port = discovery.discover_server()
print(f"Connecting to server at {host}:{port}...")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print(f"connected to server at{host}:{port} ")
while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message == "EXIT":
        print("disconnected")
        break
    print("server said", message)
    response = input("Enter your response").encode("utf-8")
    client_socket.send(response)
client_socket.close()
