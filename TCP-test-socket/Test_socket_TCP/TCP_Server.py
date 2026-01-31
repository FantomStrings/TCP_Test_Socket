import socket
import threading

HOST = "127.0.0.1"
PORT = 12000

def handle_client(conn, addr):
    with conn:
        print(f"Connected: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data.upper())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Server listening...")

    while True:
        conn, addr = server.accept()
        threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        ).start()
