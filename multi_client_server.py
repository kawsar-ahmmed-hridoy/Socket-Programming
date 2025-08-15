import socket
import threading

ip = '127.0.0.1'
port = 5000
clients = []
lock = threading.Lock()

def receive_messages(con, add):
    print(f"Connected with {add}")
    try:
        while True:
            msg = con.recv(1024).decode()
            if not msg:
                break
            print(f"{add}: {msg}")
            broadcast(f"{add}: {msg}", con)
            
    except (ConnectionResetError, OSError):
        print(f"Disconnected from {add}")
        
    finally:
        with lock:
            if con in clients:
                clients.remove(con)
        con.close()


def send_messages(con):
    try:
        while True:
            msg = input("")
            if msg.lower() == "exit":
                break
            con.send(msg.encode())
            
    except (BrokenPipeError, OSError):
        print("Connection lost")
        
    finally:
        con.close()


def broadcast(message, sender_conn):
    with lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.send(message.encode())
                except:
                    pass


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()

print(f"Server started at {ip}:{port}, waiting for connections...")

while True:
    con, add = server.accept()
    with lock:
        clients.append(con)
    threading.Thread(target=receive_messages, args=(con, add), daemon=True).start()
