
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
        self.server_socket.bind(self.host, self.port)
    
    def add_transmitter(self, transmitter):
        self.transmitters.append(transmitter)
    
    # Listen for incoming connections
    def listen(self):
        self.server_socket.listen() 
        
    def recieve_payload(self) -> DataPacket:
        data = self.server_socket.recv(1024)
        deserialized_payload = json.loads(data.decode())
        return deserialized_payload
    
    def handshake_protocol(self):
        # init_handshake = Payload.Payload(None, None, None, None)
        pass

    def run(self):
        # Accept incoming connections and handle them
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established!")

            while client_socket: # while the trasnport layer connection is open
                # Receive data from the client
                pass 
            
            client_socket.close()

class Beacon: 
    transmitter_id = 0
    def __init__(self) -> None:
        Beacon.transmitter_id += 1
        self.transmitter_id = Beacon.transmitter_id

    def send_payload(self, payload: DataPacket): 
        serialized_payload = json.dumps(payload, cls=DataPacket.PayloadEncoder)
        self.server_socket.sendall(serialized_payload.encode())
        
if __name__ == "__main__":  
    server = Server('192.168.1.15', 123456)