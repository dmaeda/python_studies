import socket

def connect_to_server(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")
        
        while True:
            data = client_socket.recv(1024)  # Receive up to 1024 bytes
            if not data:
                break  # Connection closed by server
            #print(f"Received: {data.decode('utf-8')}")
            yield f"Received: {data.decode('utf-8')}"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Client disconnected")

if __name__ == "__main__":
    connect_to_server()
