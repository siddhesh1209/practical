import socket

# Define server address and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Li
# sten for incoming connections
server_socket.listen(1)
print(f"[*] Listening ")#on {SERVER_HOST}:{SERVER_PORT}

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection")# from {client_address[0]}:{client_address[1]}

# Receive data from client
data = client_socket.recv(1024)
print("[*] Received:", data.decode())

# Send a response to client
client_socket.sendall("Hello from server!".encode())

# Close the connection
client_socket.close()
server_socket.close()


import socket

SERVER_HOST="0.0.0.0"
SERVER_PORT="0000"

servet_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_sock.bind((SERVER_PORT,SERVER_HOST))

servet_sock.listen(1)
print("listening")

client_host , client_port = servet_sock.accept()
print(" connection accepted ")

data = servet_sock.recv(1024)
print(" recieved" , data.decode())

servet_sock.sendall(" hello from server ",encode())

client_sock.close()
servet_sock.close()
