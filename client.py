import socket
import packet as DataPacket
import json 
class Client: 
    def __init__(self, client_host, server_host, server_port):
        self.client_host = client_host
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def run(self):
        
        self.client_socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

        self.perform_handshake()

        while True:
            message = input("Enter message (type 'exit' to close): ")
            if message.lower() == 'exit':
                self.send_payload(DataPacket.Payload(0, self.server_host, 0, "NCONN"))   
                break
            
            self.send_payload(DataPacket.Payload(0, self.server_host, 0, message))   

            response = self.recieve_payload()
            
            print(f"Received response: {response}")

        self.client_socket.close()

    def perform_handshake(self, client_socket):
        # Receive the server's handshake message
        handshake_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received handshake message: {handshake_message}")
        
        # Send a handshake response to the server
        message = "ACK"
        self.send_payload(DataPacket.Payload(0, self.server_host, 0, message))
        
        print("Handshake completed.")
        
    def recieve_payload(self) -> DataPacket:
        data = self.client_socket.recv(1024)
        deserialized_payload = json.loads(data.decode())
        return deserialized_payload  
    
    def send_payload(self, payload: DataPacket): 
        serialized_payload = json.dumps(payload.__dict__())
        self.client_socket.sendall(serialized_payload.encode())


if __name__ == "__main__":
    client = Client('', '192.168.1.15', 12345)
    client.run()