import numpy as np

class Plane:
    # This defines the 2D plane that all our Nodes exist on
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width


class Station:
    # This defines the base station node
    def __init__(self, stationID, posX=0, posY=0, range=0, transmitterPower=47, wavelength=0.66):
        self.stationID = stationID
        self.state = 3              # Off, T.Off, T.ON, ON
        
        # Posisiton
        self.posX = posX
        self.posY = posY
        
        # Users
        self.users = []
        
        # Physical Properties
        self.transmitterPower = transmitterPower        # in 
        self.wavelength = wavelength                    # in meters
        self.range = range                              # in meters


class User:
    # This defines the User node
    def __init__(self, userID, posX=0, posY=0, movX=0, movY=0):
        self.userID = userID
        
        # Positional
        self.posX = posX
        self.movX = movX
        self.posY = posY
        self.movY = movY
        
        # Traffic
        self.traffic = -1

    # This is used to create more/different traffic for a User
    def generateTraffic(self, seed):
        self.traffic = np.random.uniform(8, 64)
        #self.traffic = traffic.generateTraffic(seed=seed)
     

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
     
def calcDistance(node1, node2):
    return np.sqrt((node1.posX - node2.posX)**2 + (node1.posY - node2.posY)**2)

def calculateLoss(station, user):
    # Distance formula
    distance = calcDistance(user, station)
        
    # Free Space Path Loss
    loss = -10*np.log10((station.wavelength / (4*np.pi*distance))**2)
    
    # Return Loss
    return loss 

def calculateSignalStrength(transNode, recNode):
    return 0

def calculateAssociations(userArr, stationArr):
    # For Every User
    for user in userArr:
        candidate = None
        currentAssociation = None
        candidateDistance = float('inf')
        
        # For Every Station
        for station in stationArr:
            # Check if Current Association Exists
            if user in station.users:
                currentAssociation = station
            
            # Find the Distance
            distance = calcDistance(user, station)
            
            # See if this distance is in range and better than the candidate
            if (distance <= station.range) and (distance < candidateDistance) and (station.state > 1):
                candidate = station
                candidateDistance = distance            
            
        # If Candidate is not Current Association
        if not (candidate == currentAssociation):
            
            # No New Candidate
            if (candidate is None):
                # Destroy Old Association
                currentAssociation.users.remove(user)
                
            # No Old Association
            elif (currentAssociation is None):
                # Add new Association
                candidate.users.append(user)
                
            # Candidate and Current Association Both Exist
            else:
                # Add New Association
                candidate.users.append(user)
                # Destroy Old Association
                currentAssociation.users.remove(user)

def getCurrentState(stationArr, minSignal, time):
    # Declarations
    state = []
    power = 0
    mbs = stationArr[0]
    
    for station in stationArr:
        # Collect Power
        if station.state > 1: power = power + station.transmitterPower
        
        # Add Row
        state.append([time, 
                     minSignal, 
                     0,
                     station.stationID,
                     len(station.users), 
                     calculateSignalStrength(mbs, station),
                     station.state
                     ])
    
    # Add Power To Rows
    for row in state:
        row[2] = power
    
    # Return
    # FORMAT: Row > Time, Min. Signal, Power, Users, Cur. Signal, State
    return state

def applySuggestions(stationArr, stateArr):
    # Cycle Through Stations
    for index, station in enumerate(stationArr):
        match stateArr[index]:
            case 0:
                if (station.state == 3): station.state = 2                              # Move to Transition OFF
                elif (station.state == 2 or station.state == 1): station.state = 0      # Move to True OFF
            case 1:
                if (station.state == 0): station.state = 1                              # Move to Transition ON
                elif (station.state == 1 or station.state == 2): station.state = 3      # Move to True ON
                
if __name__ == "__main__":
    # Temp Variables
    station = Station(1, posX=0, posY=0, range=1000)    # Station @ [0,0]
    user = User(1, posX=10, posY=0)                     # User
    
    # Testing Calculations
    print(f"Loss = {calculateLoss(station, user)}")
            
    

        


