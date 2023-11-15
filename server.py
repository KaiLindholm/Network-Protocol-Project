
import packet as DataPacket
import socket

import protocolHandler as handler

class Server(handler.protocolHandler): 
    def __init__(self, port = 9999):
        self.host = self.get_host_ip()
        self.port = port
        self.transmitters = [] 
        # set up the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server_socket.bind((self.host, self.port))
        
    def add_transmitter(self, transmitter):
        self.transmitters.append(transmitter)
    
    # Listen for incoming connections
    def listen(self):
        self.server_socket.listen() 
        print(f"Server is listening on {self.host}:{self.port}")

    def run(self):
        # Accept incoming connections and handle them
        while True:
            print("Waiting for a connection...")
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established!")
            
            if self.handshake_protocol(client_socket, address):
                while client_socket: # while the trasnport layer connection is open
                    data = self.recieve_payload(client_socket)
                    print(f"Client {address} sent a message. {data.getData()}")
                    
                    if data.getData() == 'NCONN':
                        print(f"Client {address} has closed the connection.")
                        client_socket.close()
                        break
                    else:
                        self.send_payload(client_socket, DataPacket.Payload(0, address, 0, data.getData().upper()))
                        
                client_socket.close()
            else: 
                client_socket.close()
                continue

if __name__ == "__main__":  
    server = Server(port = 12345)
    server.listen()
    server.run()
    