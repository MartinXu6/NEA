import socket
from zeroconf import Zeroconf, ServiceInfo

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
local_IP = socket.gethostbyname(host)
print(local_IP)
port = 5000
server_socket.bind(("0.0.0.0", port))
print(f"Server started. Listening on {host}:{port}")
server_socket.listen(5)
print("Waiting for clients to connect...")
# create mDNS

zeroconf = Zeroconf()
service_info = ServiceInfo(
    "_http._tcp.local.",
    "MessageServer1._http._tcp.local.",
    addresses=[socket.inet_aton(local_IP)],
    port=5000,
    properties={},
    server = f"{host}.local"

)
zeroconf.register_service(service_info)
print(f"service registered as 'messageserver' on {local_IP}:5000")


client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

while True:
    message = input("Enter your message")
    client_socket.send(message.encode("utf-8"))
    message = client_socket.recv(1024).decode("utf-8")
    if message == "EXIT":
        print("disconnected")
        break
    print("client said",message)
zeroconf.unregister_service(service_info)
zeroconf.close()
client_socket.close()
server_socket.close()