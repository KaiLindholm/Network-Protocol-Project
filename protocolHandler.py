import packet as DataPacket
import json 
import socket

class protocolHandler:
    def recieve_payload(self, socket) -> DataPacket:
        data = socket.recv(1024)
        return DataPacket.Payload.from_json(json.loads(data.decode('utf-8')))

    def send_payload(self, socket, payload: DataPacket): 
        serialized_payload = payload.to_json()
        socket.sendall(serialized_payload.encode('utf-8'))
        
    def handshake_protocol(self, socket, address):
        
        # client sends req to server 
        # server sends ack to client 
        # cleint sends ack to server
        # handshake complete
        
        # Receive the client's handshake message
        handshake_message = self.recieve_payload(socket)
        print(f"Received handshake message: {handshake_message}")
        if handshake_message.getData() != 'REQ':
            print("Handshake failed.")
            return False
        
        # Send a handshake response to the client
        self.send_payload(socket, DataPacket.Payload(0, address, 0, "ACK"))
        
        # Receive the client's handshake message
        handshake_message = self.recieve_payload(socket)
        print(f"Received handshake message: {handshake_message}")
        
        if handshake_message.getData() == 'ACK':
            print("Handshake completed.")
            return True
        else:
            print("Handshake failed.")
            return False
        
    def get_host_ip(self):
        try:
            # get the host IP address by connecting to Google's DNS server
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(('8.8.8.8', 80))
                ip = s.getsockname()[0]
            return ip
        except socket.error as e:
            print(f"An error occurred while getting the host IP: {e}")