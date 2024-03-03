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
        self.range = range

class User:
    # This defines the User node
    def __init__(self, userID, posX=0, posY=0):
        self.userID = userID
        self.posX = posX
        self.posY = posY
        self.associatedStation = -1
        self.traffic = -1

    # This is used to create more/different traffic for a User
    def generateTraffic(self, generatedTraffic):
        self.traffic = generatedTraffic
        
    def reCalculateAssociation(self, stationArr):
        candidate = 0
        candidateDistance = float('inf')
        
        for station in stationArr:
            distance = np.sqrt((station.posX - self.posX)**2 + (station.posY - self.posY)**2)
            if distance < candidateDistance:
                candidate = station
                candidateDistance = distance
        
        self.associatedStation = candidate