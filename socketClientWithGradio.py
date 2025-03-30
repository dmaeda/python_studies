import socket
import gradio as gr
import threading
import queue
import time

data_queue1 = queue.Queue()
data_queue2 = queue.Queue()
client_socket = None

def connect_to_server(host='127.0.0.1', port=12345):
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")
        
        while True:
            data = client_socket.recv(1024)  # Receive up to 1024 bytes
            if not data:
                break  # Connection closed by server
            print(f"Received: {data.decode('utf-8')}")
            parsed_data = int(data.decode('utf-8'))  # Parse data into an integer
            if parsed_data % 2 == 0:
                data_queue1.put(parsed_data)
            else:
                data_queue2.put(parsed_data)
            #yield f"Received: {data.decode('utf-8')}"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Client disconnected")

def send_message_to_server(message):
    global client_socket
    try:
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")
        client_socket.close()
    #finally:
        

def consumer1():
    while True:
        if data_queue1.empty():
            time.sleep(0.1)
            continue
        else:
            yield data_queue1.get()

def consumer2():
    while True:
        if data_queue2.empty():
            time.sleep(0.1)
            continue
        else:
            yield data_queue2.get()

# Create Gradio interface
#with gr.Blocks() as demo:
#    output1 = gr.Textbox(label="Random Number Output1")
#    output2 = gr.Textbox(label="Random Number Output2")
#    thread1 = threading.Thread(target=connect_to_server)
#    thread1.start()
#    #connect_to_server()
#    demo.queue()
#    demo.load(consumer1, inputs=None, outputs=output1)
#    demo.load(consumer2, inputs=None, outputs=output2)


with gr.Blocks() as demo:
    with gr.Tab("Output 1"):
        output1 = gr.Textbox(label="Random Number Output1")
        send_button = gr.Button("Send 'Hello'")
        send_button.click(fn=lambda: send_message_to_server("hello"), inputs=None, outputs=None)
    with gr.Tab("Output 2"):
        output2 = gr.Textbox(label="Random Number Output2")
    
    thread1 = threading.Thread(target=connect_to_server)
    thread1.start()
    
    demo.queue()
    demo.load(consumer1, inputs=None, outputs=output1)
    demo.load(consumer2, inputs=None, outputs=output2)


# Launch the demo
demo.launch()