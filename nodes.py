import numpy as np


class Plane:
    # This defines the 2D plane that all our Nodes exist on
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width


class Station:
    # This defines the base station node
    def __init__(self, stationID, posX=0, posY=0, range=0, transmitterPower=37, gain=1, wavelength=0.0066, nodeStrength=0):
        self.stationID = stationID
        self.state = 1

        # Posisiton
        self.posX = posX
        self.posY = posY

        # Users
        self.users = []

        # Physical Properties
        self.transmitterPower = transmitterPower  # in
        self.gain = gain
        self.wavelength = wavelength  # in meters
        self.range = range  # in meters
        self.nodeStrength = nodeStrength


class User:
    # This defines the User node
    def __init__(self, userID, posX=0, posY=0, movX=0, movY=0, targ_Recv_Signal=np.random.uniform(-40, -20)):
        self.userID = userID

        # Positional
        self.posX = posX
        self.movX = movX
        self.posY = posY
        self.movY = movY

        # Traffic
        self.traffic = -1

        # Target Received Signal Strength
        self.targ_Recv_Signal = targ_Recv_Signal

    # This is used to create more/different traffic for a User
    def generateTraffic(self, seed):
        self.traffic = np.random.uniform(8, 64)
        # self.traffic = traffic.generateTraffic(seed=seed)


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
    if node1==node2:
        return 1
    return np.sqrt((node1.posX - node2.posX) ** 2 + (node1.posY - node2.posY) ** 2)


def calculateLoss(transmitter, reciever):
    # Distance formula
    distance = calcDistance(transmitter, reciever)

    # Free Space Path Loss
    loss = -10 * np.log10((transmitter.wavelength / (4 * np.pi * distance)) ** 2)

    # Return Loss
    return loss


def calculateRecievedSignalPower(transmitter, reciever):
    return transmitter.transmitterPower + 10*np.log10(transmitter.gain*1) + 20*np.log10(transmitter.wavelength) - 20*np.log10(4*np.pi) - 20*np.log10(calcDistance(transmitter, reciever))
    # return transmitter.transmitterPower + transmitter.gain - calculateLoss(transmitter, reciever)


def findUsersInRange(station, userArr):
    usersInRange = 0
    
    for user in userArr:
        if calcDistance(station, user) < station.range:
            usersInRange = usersInRange + 1
            
    return usersInRange
        
        
def calculateCellStregnth(stationArr):
    stationArr[0].nodeStrength = 1
    
    for station in stationArr[1:]:
        station.nodeStrength = calculateRecievedSignalPower(stationArr[0], station)


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
            distance = calcDistance(station, user)

            # See if this distance is in range and better than the candidate
            if (distance <= station.range) and (distance < candidateDistance) and (station.state == 1):
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

# TODO: Add Inter-Station buffer distance to prevent stations spawning on top of each other
def createPicoStations(plane, numberOfStations, buffer):
    stations = []
    
    for num in range(numberOfStations):
        # Create Station
        stations.append(Station(num+2, 
                                posX=np.random.randint(buffer, plane.width-buffer), 
                                posY=np.random.randint(buffer, plane.height-buffer), 
                                range=200, 
                                transmitterPower=25,
                                wavelength=0.007889,
                                gain=7))
        
        
    return stations
    

def getCurrentState(stationArr, userArr, minSignal, time):
    # Declarations
    state = []
    power = 0
    mbs = stationArr[0]

    for station in stationArr:
        # Collect Power
        if station.state == 1: power = power + station.transmitterPower

        # Add Row
        state.append([time,
                      minSignal,
                      0,
                      station.stationID,
                      findUsersInRange(station, userArr),
                      len(station.users),
                      station.nodeStrength,
                      station.state,
                      ])

    # Add Power To Rows
    for row in state:
        row[2] = power

    # Return
    return state


def applySuggestions(stationArr, stateArr):
    # Cycle Through Stations
    for index, station in enumerate(stationArr):
        # Apply State
        station.state = stateArr[index]


def thresholdSuggestion(stationArr, userArr, threshold):
    state = [1]
    
    # Skip the MBS
    for station in stationArr[1:]:
        if findUsersInRange(station, userArr) >= threshold:
            state.append(1)
        else:
            state.append(0)
    
    return state


if __name__ == "__main__":
    # Temp Variables
    plane = Plane(100, 100)
    station = Station(1, posX=0, posY=50, range=50, transmitterPower=22, wavelength=0.0547, gain=7)  # Station @ [0,50], 24GHZ
    userArr = [User(1, posX=10, posY=50), 
               User(2, posX=25, posY=50), 
               User(3, posX=50, posY=50),
               User(4, posX=75, posY=50),
               User(5, posX=100, posY=50),
               User(6, posX=500, posY=50)]  # Users

    # Testing RSRP Calculations
    for user in userArr:
        print(f"User {user.userID} RSS = {calculateRecievedSignalPower(station, user):.2f} dBm")
