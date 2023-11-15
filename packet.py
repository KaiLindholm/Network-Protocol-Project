
import json

class Payload: 
    def __init__(self, cone_ID = 0, destIPAddr = '', packet_ID = 0, data_len = 0, data = '123'):
        self.cone_ID = cone_ID
        self.destIPAddr = destIPAddr            # the destination address of the packet
        self.packet_ID = packet_ID              
        self.data_len = len(data)    # the length of the data payload
        self.data = data        # the data payload
    
    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def getData(self):
        return self.data
    
    def __str__(self):
        return f"Payload: Cone_ID={self.cone_ID}, IP_Address={self.destIPAddr}, Packet_ID={self.packet_ID}, Data_Length={self.data_len}, payload={self.data}"
    
    def to_dict(self):
        return {'cone_ID': self.cone_ID, 
                'destIPAddr': self.destIPAddr, 
                'packet_ID': self.packet_ID, 
                'data_len': self.data_len, 
                'data': self.data}