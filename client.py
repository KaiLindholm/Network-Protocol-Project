import packet as DataPacket
import socket

import protocolHandler as handler

class Client(handler.protocolHandler): 
    def __init__(self, server_host, server_port):
        self.client_host = self.get_host_ip()
        self.server_host = server_host
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(4)                   # set a timeout of 4 seconds

    def run(self):
        try:
            self.socket.connect((self.server_host, self.server_port))
        except socket.error as e:
            print(f"An error occurred while connecting to the server: {e}")
            return
        
        print(f"Connected to server at {self.server_host}:{self.server_port}")

        # intiate handshake protocol
        # send REQ 
        self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "REQ"))
        
        # check if server responds with ACK        
        try:
            # check if server responds with ACK        
            if self.recieve_payload(self.socket).getData() == 'ACK':
                print("Handshake successful.")
            else: 
                print("Handshake failed.")
                self.socket.close()
                return
        except socket.timeout:
            print("Handshake timed out.")
            self.socket.close()
            return
        
        print("Enter 'exit' to close the connection.")
        while True:
            message = ""
            while not message:
                message = input("$ ")
                
            if message.lower() == 'exit':
                self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, "NCONN"))   
                break
        
            if not self.send_payload(self.socket, DataPacket.Payload(0, self.server_host, 0, message)):   # check if the payload was sent successfully
                res = self.recieve_payload(self.socket) 
                if not res:
                    print("Server has closed the connection.")
                    break
                else:
                    print(res.getData())
                    
                if res.getData() == 'NCONN':
                    print("Server has closed the connection.")
                    break
            else:       # if not the server has either closed the connection or the connection has timed out
                print("Server has closed the connection.")
                break

        print("Closing connection...")
        self.socket.close()
        
if __name__ == "__main__":
    print("Enter the server's IP address.")
    server_host = input("Server IP: ")
    print("Enter the server's port.")
    server_port = int(input("Server Port: "))
    
    print("--------------------------------------")
        
    client = Client(server_host, server_port)
    try:
        client.run()
    except KeyboardInterrupt:
        client.send_payload(client.socket, DataPacket.Payload(0, client.server_host, 0, "NCONN"))
        client.socket.close()
        exit(0)
        
        