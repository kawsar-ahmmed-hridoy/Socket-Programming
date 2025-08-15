# Socket Programming: Combined Chat & File Server Application

A simple TCP socket-based chat application written in Python, supporting multiple clients via threading.

## 📌 Features
- **Multiple Clients**: Many clients can connect to the server at the same time.
- **Real-Time Chat**: Messages are broadcast to all connected clients.
- **Threaded Connections**: Each client is handled in a separate thread for simultaneous communication.
- **Exit Command**: Type `exit` in a client to disconnect gracefully.

---

## 📂 Project Structure

📁 Socket-Chat
 ├── server.py   # Multi-client server
 ├── client.py   # Client application
 ├── multi_client_server.py # Multi-client server
 ├── image.png # Visualization
 └── README.md   # This documentation

---

## ⚙️ Requirements
- Python **3.7+** (Tested with Python 3.10+)
- No external dependencies (uses Python's built-in `socket` and `threading`)

---

## 🚀 How to Run (bash)

### 1️⃣ Start the Server

python server.py

### 2️⃣ Start a Client

python client.py

### 3️⃣ Connect More Clients

python multi_client_server.py

python client1.py

python client2.py

python client3.py


