import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "0.0.0.0"
port = 12345
server_socket.bind((host, port))
print(f"Server started. Listening on {host}:{port}")
server_socket.listen(5)
print("Waiting for clients to connect...")
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message == "EXIT":
        print("disconnected")
        break
    print("client said",message)
    response = input("Enter your response")
    client_socket.send(response.encode('utf-8'))
client_socket.close()
server_socket.close()