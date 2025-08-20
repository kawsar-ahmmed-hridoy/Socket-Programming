# 🖧 Socket Programming in Python

This project demonstrates **basic socket programming** concepts in Python through two tasks:  
1. **Chatting with server-client (single & multi-client)**  
2. **File Manipulation (list, upload, download, delete)**  

---

## 📂 Project Structure

```

SOCKET PROGRAMMING/
│
├── Task1-Chatting with server-client/
│   ├── client.py                    # Simple chat client
│   ├── server.py                    # Single client chat server
│   └── multi_client_server.py     # Multi-client chat server
│
├── Task2-File Manipulation/
│   ├── server_files           # Store uploaded files
│   ├── file_client.py         # Client for file operations
│   └── file_server.py         # Server for file operations
│
├── image.png                  # Visualization of building connection
├── Folder                     # Store files initially
└── README.md                  # Directions

````

## ⚙️ Requirements

- Python 3.x  
- No external libraries required (uses built-in `socket`, `threading`, `os`)  

---

## 🚀 How to Run

### 🔹 Task 1: Chatting with Server-Client

#### Single Client
1. Run the server:

   python 'Task1-Chatting with server-client'/server.py


2. Run the client (in a separate terminal):

   python 'Task1-Chatting with server-client'/client.py


#### Multi-Client

1. Run the multi-client server:

   python 'Task1-Chatting with server-client'/multi_client_server.py

2. Run multiple clients in different terminals:

   python 'Task1-Chatting with server-client'/client.py
   

---

### 🔹 Task 2: File Manipulation

#### Start the Server


python 'Task2-File Manipulation'/file_server.py


#### Start the Client


python 'Task2-File Manipulation'/file_client.py


#### Available Commands

Inside the client, you can enter:

* `list` → Show files on the server
* `upload <filename>` → Upload file to server
* `download <filename>` → Download file from server
* `delete <filename>` → Delete file from server
* `exit` → Disconnect

---

## 📌 Notes

* Run server **before** running the client.
* Use `127.0.0.1` (localhost) to test locally.
* Modify `ip` and `port` in scripts if needed.

---

## 🏆 Learning Outcomes

* Understanding **socket communication** (TCP).
* Handling **multiple clients** using `threading`.
* Implementing **file transfer protocols** with sockets.

---

✍️ Author: Kawsar Ahmmed Hridoy

```