import numpy as np
import gen_user_requests as traffic

class Plane:
    # This defines the 2D plane that all our Nodes exist on
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

class Station:
    # This defines the base station node
    def __init__(self, stationID, posX=0, posY=0, range=0, transmitterGain=5, transmitterPower=25, wavelength=0.07):
        self.stationID = stationID
        self.posX = posX
        self.posY = posY
        self.users = []
        self.transmitterGain = transmitterGain          # in dBm
        self.transmitterPower = transmitterPower        # in dBm
        self.wavelength = wavelength                    # in m
        self.range = range
        #self.range = self.calcMaxRange()               # in m
   
    def calcMaxRange(self, Gr=1, minQuality=-80):
        # Uses RSSI db, min -80db
        # TODO: Currently Busted
        firstTerm = self.transmitterGain * Gr * np.power(self.wavelength, 2)
        print(f"First Term:\t{firstTerm}")
        
        secondTerm = np.power(4*np.pi, 2)
        print(f"Second Term:\t{secondTerm}")
        
        thirdTerm = self.transmitterPower / minQuality
        print(f"Third Term:\t{thirdTerm}")
        
        result = np.sqrt((firstTerm/secondTerm) * -thirdTerm)
        print(f"Max Range:\t{result}")
        
        self.range = result


class User:
    # This defines the User node
    def __init__(self, userID, posX=0, posY=0, movX=0, movY=0):
        self.userID = userID
        self.posX = posX
        self.movX = movX
        self.posY = posY
        self.movY = movY
        
        
        self.traffic = -1

    # This is used to create more/different traffic for a User
    def generateTraffic(self, seed):
        self.traffic = np.random.uniform(8, 64)
        self.traffic = traffic.generateTraffic(seed=seed)
     
def generateUsers(plane, numberOfUsers, speed):
    userArr = []
    
    # Generating Users
    for element in range(numberOfUsers):
        userArr.append(User(element, 
                            posX=np.random.uniform(0, plane.width), 
                            posY=np.random.uniform(0, plane.height), 
                            movX=np.random.uniform(-speed, speed), 
                            movY=np.random.uniform(-speed, speed)))
    
    # Return
    return userArr
     

def calculateSignalStrength(user, station):
    # Distance formula
    distance = np.sqrt((station.posX - user.posX)**2 + (station.posY - user.posY)**2)
        
    # Free Space Path Loss (((4pi*r)/Lam)^2)
    loss = ((4*np.pi*distance) / station.wavelength)**2
    
    # Relative RSSI (Pt + Gt - L)
    rssi =  station.transmitterGain + station.transmitterPower - loss
    
    return rssi 
          
def calculateAssociations(userArr, stationArr):
    # For Every User
    for user in userArr:
        candidate = None
        currentAssociation = None
        candidateDistance = float('inf')
        
        # For Every Station
        for station in stationArr:
            # Check if Current Association
            if user in station.users:
                currentAssociation = station
            
            # Find the Distance
            distance = np.sqrt((station.posX - user.posX)**2 + (station.posY - user.posY)**2)
            
            # See if this distance is in range and better than the candidate
            if distance <= station.range and distance < candidateDistance:
                candidate = station
                candidateDistance = distance
        
        if candidate is not None:  # Check if a valid candidate was found
            # If Candidate is not Current Association
            if not (candidate == currentAssociation):
                # Add New Association
                candidate.users.append(user)
                if (currentAssociation is not None):
                    # Destroy Old Association
                    currentAssociation.users.remove(user)
                
            
        

            
    

        


