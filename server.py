import socket
import threading
ip = '127.0.0.1'
port = 5000
#socket = ip + port

def receive_messages(con, add):
    print(f"Connected with {add}")
    try:
        while True:
            msg = con.recv(1024).decode()
            if not msg:
                break
            print(f"Client: {msg}")
            
    except (ConnectionResetError, OSError):
        print(f"Disconnected from {add}! Re-establish connection.")
        
    finally:
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



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f"Server started at {ip}:{port}, waiting for connection...")

con, add = server.accept()

threading.Thread(target=receive_messages, args=(con, add), daemon=True).start()
send_messages(con)
