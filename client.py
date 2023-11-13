import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}")

    perform_handshake(client_socket)

    while True:
        message = input("Enter message (type 'exit' to close): ")
        if message.lower() == 'exit':
            break

        client_socket.sendall(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received response: {response}")

    client_socket.close()

def perform_handshake(client_socket):
    # Receive the server's handshake message
    handshake_message = client_socket.recv(1024).decode('utf-8')
    print(f"Received handshake message: {handshake_message}")

    # Send a handshake response to the server
    response_message = "Hello, server! Let's start messaging."
    client_socket.sendall(response_message.encode('utf-8'))

    print("Handshake completed.")

if __name__ == "__main__":
    start_client()
