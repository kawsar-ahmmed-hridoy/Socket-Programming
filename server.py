import socket
import threading


def receive_messages(con, add):
    print(f"Connected with {add}")
    try:        
        while True:
            msg = con.recv(1024).decode()
            if not msg:
                break
            
            print(f"Client with address {add}: {msg}")            
    except:
        print(f"Disconnected! Re-establish Connection")        
    finally:
        con.close()
        

def send_messages(con):
    try:
        while True:
            msg = input("")
            if msg.lower() == "exit":
                break
            con.send(msg.encode())
    except:
        pass
    finally:
        con.close()
            


ip = '127.0.0.1'
port = 5000
#Socket = ip + port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((ip, port))
server.listen(1)

print(f"Waiting for connection...")

con, add = server.accept()

print(f"Connection established💡")

threading.Thread(target=receive_messages, args=(con, add), daemon=True).start()
send_messages(con)
