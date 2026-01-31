import socket

HOST = "127.0.0.1"
PORT = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.settimeout(5)
    client.connect((HOST, PORT))
    msg = input("Enter lowercase message: ")
    client.sendall(msg.encode())
    reply = client.recv(1024)
    print("From server:", reply.decode())