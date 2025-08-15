import socket
import threading
ip = '127.0.0.1'
port = 5000

def receive_messages(client):
    try:        
        while True:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(f"\nServer: {msg}")
            
    except (ConnectionResetError, OSError):
        print("\n[Disconnected from server]")
        
    finally:
        client.close()


def send_messages(client):
    try:
        while True:
            msg = input("")
            if msg.lower() == "exit":
                break
            client.send(msg.encode())
            
    except (BrokenPipeError, OSError):
        print("\n[Connection lost]")
        
    finally:
        client.close()



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"[Connecting to {ip}:{port}]")
    client.connect((ip, port))
    print(f"[Connected to server]")
except:
    print(f"[Failed to connect]")
    exit()

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
send_messages(client)
