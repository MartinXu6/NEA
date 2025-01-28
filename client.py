import socket

host = "iphone"
port = 5000

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
print(f"connected to server at{host}:{port} ")
while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message == "EXIT":
        print("disconnected")
        break
    print("server said",message)
    response = input("Enter your response").encode("utf-8")
    client_socket.send(response)
client_socket.close()
