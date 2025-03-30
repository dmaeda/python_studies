import socket
import gradio as gr
import random
import threading
import queue
import time

data_queue1 = queue.Queue()
data_queue2 = queue.Queue()

def generate_random1():
    while True:
        #yield random.randint(1, 100) 
        number = random.randint(1, 100)
        print(f"Generated: {number}")
        # Simulate some processing time
        if number % 2 == 0:
            data_queue1.put(number)
            #yield number
        else:
            data_queue2.put(number)
            #yield number
        time.sleep(1)
        
def generate_random2():
    while True:
        yield random.randint(1, 100) 

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
with gr.Blocks() as demo:
    output1 = gr.Textbox(label="Random Number Output1")
    output2 = gr.Textbox(label="Random Number Output2")
    thread1 = threading.Thread(target=generate_random1)
    thread1.start()
    # Queue for live updates with continuous streaming
    #connect_to_server()
    demo.queue()
    demo.load(consumer1, inputs=None, outputs=output1)
    demo.load(consumer2, inputs=None, outputs=output2)
# Launch the demo
demo.launch()