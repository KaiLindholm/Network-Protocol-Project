
import socket

# Define the server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send data to the server
data = 'Hello, server!'
client_socket.sendall(data.encode())

# Receive data from the server
received_data = client_socket.recv(1024)
print(received_data.decode())

# Close the socket
client_socket.close()
