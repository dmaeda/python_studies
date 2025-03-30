import socket
import random
import time

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one client
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            print("Waiting for connection...")
            client_socket, client_address = server_socket.accept()
            print(f"Connected to {client_address}")
            
            try:
                while True:
                    random_number = random.randint(1, 999)
                    client_socket.sendall(str(random_number).encode('utf-8'))
                    print(f"Sent: {random_number}")
                    time.sleep(0.5)  # Wait for 500 milliseconds
            except BrokenPipeError:
                print("Connection closed by client")
                client_socket.close()
            except Exception as e:
                print(f"Error: {e}")
                client_socket.close()
    finally:
        server_socket.close()
        print("Server shut down")

if __name__ == "__main__":
    start_server()