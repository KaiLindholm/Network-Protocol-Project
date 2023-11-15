import packet as DataPacket
import json 
import socket

import protocolHandler as handler

class Client(handler.protocolHandler): 
    def __init__(self, server_host, server_port):
        self.client_host = self.get_host_ip()
        self.server_host = server_host
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def run(self):
        self.socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

        # intiate handshake protocol
        # send REQ 
        
        self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, data="REQ"))
        
        while True:
            message = input("Enter message (type 'exit' to close): ")
            if message.lower() == 'exit':
                self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "NCONN"))   
                break
            
            self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, message))   

            response = self.recieve_payload()
            
            print(f"Received response: {response}")

        self.socket.close()

    def perform_handshake(self):
        # Receive the server's handshake message
        handshake_message = self.socket.recv(1024).decode('utf-8')
        print(f"Received handshake message: {handshake_message}")
        
        # Send a handshake response to the server
        self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "ACK"))
        
        print("Handshake completed.")
        
if __name__ == "__main__":
    client = Client('192.168.4.31', 12345)
    client.run()