import packet as DataPacket
import json 
import socket

class protocolHandler:
    def recieve_payload(self, socket) -> DataPacket:
        data = socket.recv(1024)
        if not data:
            return None
        
        return DataPacket.Payload.from_json(json.loads(data.decode('utf-8')))

    def send_payload(self, socket, payload: DataPacket): 
        serialized_payload = payload.to_json()
        socket.sendall(serialized_payload.encode('utf-8'))
        
    def get_host_ip(self):
        try:
            # get the host IP address by connecting to Google's DNS server
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(('8.8.8.8', 80))
                ip = s.getsockname()[0]
            return ip
        except socket.error as e:
            print(f"An error occurred while getting the host IP: {e}")