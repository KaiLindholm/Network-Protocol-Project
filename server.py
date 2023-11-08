
import socket

# Define the host and port to listen on
HOST = 'localhost'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Accept incoming connections and handle them
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")
    
    # TODO: Implement custom network protocol logic here
    
    client_socket.close()
