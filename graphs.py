import gen_user_requests as usr_req
import matplotlib.pyplot as plt
import nodes
import numpy as np



# graphing power vs time
def GraphingPvsT(time=0, power=1, dataReq=1):
    # Time Frame to Graph in sec (1 sec, 60 sec, 3600 sec, etc.)
    # Power in Watts over 1 sec time frames
    # Required Data Rate over 1 sec time frame
    
    # Temp Stuff
    time = 60
    arr = usr_req.generateTraffic(maxDataSize=256, trafficStyle=2, dataRange=12, totalrequests=60)

    # Power
    power = [t[1] for t in arr]
    newNum = 0
    newArr = []
    
    for i in range(len(power)):
        if i%15 == 0:
            newNum = power[i]
        newArr.append(newNum)
        
        
    # Plotting
    # TODO: Fix this so that the colors show correctly
    plt.bar(np.arange(1, time+1), newArr, color='red')                      # Ideal Scenario
    plt.bar(np.arange(1, time+1), power, color='blue')                      # Service Coverage Losses
    plt.plot(np.arange(1, time+1), power, color='green')                    # Actual Data Rate
    plt.show()
        
# This function is used to graph the current situation from the data provided
# It takes the plane object, as well as the station and user objects (both in the form of arrays) as input
def plotFrame(stationArr, userArr):
    # Add the Stations
    # TODO: Add Tapered Effect to the circle, indicating the loss of signal strength over distance
    for station in stationArr:
        plt.scatter(station.posX, station.posY, color='black', marker='o', label=None)
        plt.gca().add_patch(plt.Circle((station.posX, station.posY), station.range, color='gray', alpha=0.2))
    
    # Add the Users
    for user in userArr:
        plt.scatter(user.posX, user.posY, color='blue', marker='o', label=None)
    
    # Plot Associations
    for station in stationArr:
        for user in station.users:
            plt.plot([user.posX, station.posX], [user.posY, station.posY], color='green', label=None)
    
    # Return
    plt.grid(True)
    return

def updatePositions(plane, userArr):
    # Loop through all Users
    for user in userArr:
        # Find New Locations
        newPosX = user.posX + user.movX
        newPosY = user.posY + user.movY
        
        # Check X Bounds
        if (newPosX>0) and (newPosX<plane.width):
            user.posX = newPosX
        else:
            user.movX = -1*user.movX
            user.posX = user.posX + user.movX
            
        # Check Y Bounds
        if (newPosY>0) and (newPosY<plane.height):
            user.posY = newPosY
        else:
            user.movY = -1*user.movY
            user.posY = user.posY + user.movY    
    
if __name__ == "__main__":
    GraphingPvsT(1, 1, 1)