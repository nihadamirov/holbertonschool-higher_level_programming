#!/usr/bin/env python3
import socket
import json
import threading
import time

def start_server(host='localhost', port=65432):
    """Start the server to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        data = conn.recv(1024)
        if not data:
            break

        try:
            received_dict = json.loads(data.decode())
            print("Received Dictionary from Client:")
            print(received_dict)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        conn.close()

def send_data(data, host='localhost', port=65432):
    """Send a dictionary to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        serialized_data = json.dumps(data).encode()
        client_socket.sendall(serialized_data)
    except ConnectionError as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
