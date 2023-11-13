
import socket
import json

import packet as DataPacket
import beaconPacket as BeaconPacket
class Server: 
    def __init__(self, host, port):
        self.host = host
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
        
    def recieve_payload(self) -> DataPacket:
        data = self.server_socket.recv(1024)
        deserialized_payload = json.loads(data.decode())
        return deserialized_payload

    def send_payload(self, client_socket, payload: DataPacket): 
        serialized_payload = json.dumps(payload.__dict__())
        client_socket.sendall(serialized_payload.encode())
        
    def handshake_protocol(self, client_socket, client_address):  
        # Send a handshake message to the client
        handshake_message = "ACK"
        self.send_payload(client_socket, DataPacket.Payload(0, client_address, 0, handshake_message))
        # Receive the client's handshake response
        response_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received handshake response: {response_message}")

        if response_message == "ACK": 
            print("Handshake completed.")
            return True
        else: 
            print("Handshake failed.")
            return False
        
    def run(self):
        # Accept incoming connections and handle them
        while True:
            print("Waiting for a connection...")
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established!")
            
            if self.handshake_protocol(client_socket, address):
                while client_socket: # while the trasnport layer connection is open
                    pass
                
                client_socket.close()
            else: 
                client_socket.close()
                continue

class Beacon: 
    transmitter_id = 0
    def __init__(self) -> None:
        Beacon.transmitter_id += 1
        self.transmitter_id = Beacon.transmitter_id

        
if __name__ == "__main__":  
    server = Server('192.168.1.15', 12345)
    server.listen()
    server.run()