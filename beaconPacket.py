
class BeaconPacket:
    num_cones = 0
    def __init__(self):
        BeaconPacket.num_cones += 1
        self.Cone_ID = BeaconPacket.num_cones           # the cone ID is created via the server a handshake is successful.
        self.identifier = None                  # the identifier is a negative number to distgusih the IP address in the data packets
    
    def isValid(self):
        return self.Cone_ID > 0
    
    def set_identifier(self, identifier):
        self.identifier = identifier