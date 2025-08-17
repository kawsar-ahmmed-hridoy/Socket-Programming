import socket
import os

ip = '127.0.0.1'
port = 6000


def list_files(client):
    print(client.recv(4096).decode())


def upload_file(client, filename):
    if os.path.exists(filename):
        if client.recv(1024) == b"READY":
            with open(filename, "rb") as f:
                for chunk in iter(lambda: f.read(1024), b''):
                    client.send(chunk)
            client.send(b"EOF")
            print(client.recv(1024).decode())
    else:
        print("File not found.")


def download_file(client, filename):
    if client.recv(1024) == b"READY":
        with open(filename, "wb") as f:
            while True:
                data = client.recv(1024)
                if data == b"EOF":
                    break
                f.write(data)
        print("Download complete.")
    else:
        print("File not found on server.")


def delete_file(client, filename):
    print(client.recv(1024).decode())



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"[Connecting to {ip}:{port}]")
    client.connect((ip, port))
    print("[Connected to server]")
except Exception as e:
    print(f"Connection error: {e}")
    exit()

while True:
    cmd = input("\nEnter command (list, upload <file>, download <file>, delete <file>, exit): ").strip()
    if not cmd:
        continue

    client.send(cmd.encode())
    parts = cmd.split(" ", 1)
    action = parts[0].lower()

    if action == "list":
        list_files(client)

    elif action == "upload" and len(parts) > 1:
        upload_file(client, parts[1])

    elif action == "download" and len(parts) > 1:
        download_file(client, parts[1])

    elif action == "delete" and len(parts) > 1:
        delete_file(client, parts[1])

    elif action == "exit":
        print(client.recv(1024).decode())
        break

    else:
        print(client.recv(1024).decode())

client.close()
print("[Disconnected]")
