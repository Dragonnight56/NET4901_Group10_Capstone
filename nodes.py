import numpy as np
import gen_user_requests as traffic

class Plane:
    # This defines the 2D plane that all our Nodes exist on
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width


class Station:
    # This defines the base station node
    # TODO: Change Range to Actual Technical Specs (Channel Gain, Etc.)
    def __init__(self, stationID, posX=0, posY=0, range=0):
        self.stationID = stationID
        self.posX = posX
        self.posY = posY
        self.users = []
        self.range = range
        # set of currently connected users

class User:
    # This defines the User node
    def __init__(self, userID, posX=0, posY=0):
        self.userID = userID
        self.posX = posX
        self.posY = posY
        self.traffic = -1
        # set of possible stations based on range

    # This is used to create more/different traffic for a User
    def generateTraffic(self, seed):
        self.traffic = traffic.generateTraffic(seed)
        
def calculateAssociations(userArr, stationArr):
    # For Every User
    for user in userArr:
        candidate = None
        candidateDistance = float('inf')
        
        # For Every Station
        for station in stationArr:
            # Find the Distance
            distance = np.sqrt((station.posX - user.posX)**2 + (station.posY - user.posY)**2)
            
            # See if this distance is in range and better than the candidate
            if distance <= station.range and distance < candidateDistance:
                candidate = station
                candidateDistance = distance
        
        if candidate is not None:  # Check if a valid candidate was found
            candidate.users.append(user)
        

            
    

        


