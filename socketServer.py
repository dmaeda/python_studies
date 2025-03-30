import socket
import random
import time
import threading

def handle_client_receive(client_socket):
    """Thread to handle receiving data from the client."""
    try:
        while True:
            data = client_socket.recv(1024)  # Receive up to 1024 bytes
            if not data:
                print("Client disconnected")
                break
            print(f"Received from client: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Error in receiving thread: {e}")
    finally:
        client_socket.close()

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
            
            # Start a thread to handle receiving data from the client
            receive_thread = threading.Thread(target=handle_client_receive, args=(client_socket,))
            receive_thread.start()
            
            try:
                while True:
                    # Send a random number to the client
                    random_number = random.randint(1, 999)
                    client_socket.sendall(str(random_number).encode('utf-8'))
                    print(f"Sent: {random_number}")
                    time.sleep(0.5)  # Wait for 500 milliseconds
            except BrokenPipeError:
                print("Connection closed by client")
                break
            except Exception as e:
                print(f"Error: {e}")
                break
    finally:
        server_socket.close()
        print("Server shut down")

if __name__ == "__main__":
    start_server()