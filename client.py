import socket

host = "local host"
port = 5000

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",port))
while True:
    message = client_socket.recv(1024)
    if message == "EXIT":
        print("disconnected")
        break
    print("server said",message)
    response = input("Enter your response")
    client_socket.send(response)
client_socket.close()
