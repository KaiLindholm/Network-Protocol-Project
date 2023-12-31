import packet as DataPacket
import socket

import protocolHandler as handler

class Server(handler.protocolHandler): 
    def __init__(self, port = 9999):
        self.host = self.get_host_ip()
        self.port = port
        # self.transmitters = [] 
        # set up the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server_socket.bind((self.host, self.port))
        
    # def add_transmitter(self, transmitter):     # not implementing multithreading for multiple clients
    #     self.transmitters.append(transmitter)
    
    # Listen for incoming connections
    def listen(self):
        self.server_socket.listen(1) 
        print(f"Server is listening on {self.host}:{self.port}")

    def run(self):
        # Accept incoming connections and handle them
        while True:
            print("Waiting for a connection...")
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established!")
            
            message = self.recieve_payload(client_socket)
            print(f"Received handshake message: {message}")
            check = message.getData() == 'REQ'; 

            if check:
                print("Handshake Initiator: Sending ACK")
                self.send_payload(client_socket, DataPacket.Payload(0, address, 0, 'ACK'))
            else: 
                print('Handshake failed.')
                client_socket.close()
                continue
            
            if check:   # the handshake was successful
                while client_socket: # while the trasnport layer connection is open
                    data = self.recieve_payload(client_socket)
                    if data:
                        print(f"Client {address} sent a message. {data.getData()}")
                        
                        if data.getData() == 'NCONN':
                            print(f"Client {address} has closed the connection.")
                            client_socket.close()
                            break
                        else:
                            self.send_payload(client_socket, DataPacket.Payload(0, address, 0, data.getData()))
            else: 
                print('Handshake failed.')
                client_socket.close()
                continue

if __name__ == "__main__":  
    server = Server(port = 3002)
    server.listen()
    try:
        server.run()
    except KeyboardInterrupt:
        print("\nClosing server...")
        server.send_payload(server.server_socket, DataPacket.Payload(0, server.host, 0, "NCONN"))
        server.server_socket.close()
        exit(0)
        
    