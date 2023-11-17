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
        self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "REQ"))
        
        # check if server responds with ACK        
        if self.recieve_payload(self.socket).getData() == 'ACK':
            print("Handshake successful.")
        else: 
            print("Handshake failed.")
            print(res)
            self.socket.close()
            return
        
        while True:
            message = input("$ ")
            if message.lower() == 'exit':
                self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "NCONN"))   
                break
            
            self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, message))  
            
            res = self.recieve_payload(self.socket) 
            print("ECHO: " + res.getData())
        print("Closing connection...")
        self.socket.close()
        
if __name__ == "__main__":
    print("Enter the server's IP address.")
    server_host = input("Server IP: ")
    print("Enter the server's port.")
    server_port = int(input("Server Port: "))
    
    print("--------------------------------------")
        
    print("Enter 'exit' to close the connection.")
    client = Client(server_host, server_port)
    try:
        client.run()
    except KeyboardInterrupt:
        print("Closing connection...")
        client.send_payload(client.socket, DataPacket.Payload(0, client.server_host, 0, "NCONN"))
        client.socket.close()
        print("Connection closed.")
        exit(0)
        
        