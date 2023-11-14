
import json

class Payload:
    class PayloadEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Payload):
                return obj.__dict__
            return json.JSONEncoder.default(self, obj)
        
    def __init__(self, Cone_ID = 0, IP_Address = '', Packet_ID =0, Data_Payload = ''):
        self.Cone_ID = Cone_ID
        self.IP_Address = IP_Address            # the destination address of the packet
        self.Packet_ID = Packet_ID              
        self.Data_Length = len(Data_Payload)    # the length of the data payload
        self.Data_Payload = Data_Payload        # the data payload
    
    def setCone_ID(self, Cone_ID): # the cone ID is created via the server a handshake is successful. 
        self.Cone_ID = Cone_ID
        
    def setIP_Address(self, IP_Address): # the destination address of the packet
        self.IP_Address = IP_Address

    def setPacket_ID(self, Packet_ID):
        self.Packet_ID = Packet_ID
    
    def getData(self):
        return self.Data_Payload    
    
    def __dict__(self):
        return {
            'Cone_ID': self.Cone_ID,
            'IP_Address': self.IP_Address,
            'Packet_ID': self.Packet_ID,
            'Data_Length': self.Data_Length,
            'Data_Payload': self.Data_Payload
        }
        
    def fromDict(self, df):
        self.Cone_ID = df['Cone_ID']
        self.IP_Address = df['IP_Address']
        self.Packet_ID = df['Packet_ID']
        self.Data_Length = df['Data_Length']
        self.Data_Payload = df['Data_Payload']
        return self
    def __str__(self):
        return f"Payload: Cone_ID={self.Cone_ID}, IP_Address={self.IP_Address}, Packet_ID={self.Packet_ID}, Data_Length={self.Data_Length}, Data_Payload={self.Data_Payload}"