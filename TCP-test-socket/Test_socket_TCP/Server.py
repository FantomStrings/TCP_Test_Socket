import socket

HOST = "::1"
PORT = 12000

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("IPv6 server listening...")

    conn, addr = server.accept()
    with conn:
        data = conn.recv(1024)
        if data:
            conn.sendall(data.upper())
