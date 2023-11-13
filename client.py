import socket
import packet as DataPacket
import json 
class Client: 
    def __init__(self, client_host, server_host, server_port):
        self.client_host = client_host
        self.server_host = server_host
        self.server_port = server_port
        
    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

        self.perform_handshake(client_socket)

        while True:
            message = input("Enter message (type 'exit' to close): ")
            if message.lower() == 'exit':
                self.send_payload(DataPacket.Payload(0, self.client_host, 0, "NCONN"))   
                break
            
            client_socket.send(DataPacket.Payload(0, self.client_host, 0, message).encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received response: {response}")

        client_socket.close()

    def perform_handshake(self, client_socket):
        # Receive the server's handshake message
        handshake_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received handshake message: {handshake_message}")
        
        # Send a handshake response to the server
        meesage = "ACK"
        client_socket.send(DataPacket.Payload(0, self.client_host, 0, meesage).encode('utf-8'))

        print("Handshake completed.")
        
    def send_payload(self, payload: DataPacket): 
        serialized_payload = json.dumps(payload, cls=DataPacket.PayloadEncoder)
        self.client_socket.sendall(serialized_payload.encode())


if __name__ == "__main__":
    client = Client('', '192.168.1.15', 12345)
    client.run()