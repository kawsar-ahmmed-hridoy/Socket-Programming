import socket
import threading
import os

ip = '127.0.0.1'
port = 6000
folder = "server_files"
os.makedirs(folder, exist_ok=True)

def list_files(folder):
    files = os.listdir(folder)
    if files:
        return "\n".join(files)
    else:
        return "No files."



def upload_file(con, filename):

    con.send(b"READY")
    with open(os.path.join(folder, filename), "wb") as f:
        while True:
            data = con.recv(1024)
            if data == b"EOF":
                break
            f.write(data)
    con.send(b"UPLOAD DONE")


def download_file(con, filename):

    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        con.send(b"READY")
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(1024), b''):
                con.send(chunk)
        con.send(b"EOF")
    else:
        con.send(b"FILE NOT FOUND")


def delete_file(con, filename):

    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        con.send(b"DELETE DONE")
    else:
        con.send(b"FILE NOT FOUND")


def handle_client(con, add):

    print(f"Connected with {add}")
    
    try:
        while True:
            command = con.recv(1024).decode()
            if not command:
                break

            cmd_parts = command.strip().split(" ", 1)
            cmd = cmd_parts[0].lower()

            if cmd == "list":
                con.send(list_files().encode())

            elif cmd == "upload" and len(cmd_parts) > 1:
                upload_file(con, cmd_parts[1])

            elif cmd == "download" and len(cmd_parts) > 1:
                download_file(con, cmd_parts[1])

            elif cmd == "delete" and len(cmd_parts) > 1:
                delete_file(con, cmd_parts[1])

            elif cmd == "exit":
                break

            else:
                con.send(b"INVALID COMMAND")

    except (ConnectionResetError, OSError):
        print(f"Disconnected from {add}! Re-establish connection.")

    finally:
        con.close()
        print(f"Connection closed with {add}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

print(f"File server started at {ip}:{port}, waiting for connections...")

while True:
    con, add = server.accept()
    threading.Thread(target=handle_client, args=(con, add), daemon=True).start()
