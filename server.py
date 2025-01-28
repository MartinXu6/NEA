import socket

server_socket = socket.socket()
host = socket.gethostname()
port = 5000
server_socket.bind((host, port))
print(f"Server started. Listening on {host}:{port}")
server_socket.listen(5)
print("Waiting for clients to connect...")
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
client_socket.close()
server_socket.close()