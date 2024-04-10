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
    #plt.plot(np.arange(1, time+1), newArr, color='red')                      # Ideal Scenario
    #plt.plot(np.arange(1, time+1), power, color='blue')                      # Service Coverage Losses
    #plt.plot(np.arange(1, time+1), power, color='green')                    # Actual Data Rate
    plt.show()
        
# This function is used to graph the current situation from the data provided
# It takes the plane object, as well as the station and user objects (both in the form of arrays) as input
def plotFrame(stationArr, userArr, RED, YELLOW):
    # Add the Stations
    # TODO: Add Tapered Effect to the circle, indicating the loss of signal strength over distance
    for station in stationArr:
        plt.scatter(station.posX, station.posY, color='black', marker='o', label=None)
        if (station.state == 1):
            plt.gca().add_patch(plt.Circle((station.posX, station.posY), nodes.calculateExRange(station, RED), color='gray', alpha=0.2))
    
    # Add the Users
    for user in userArr:
        plt.scatter(user.posX, user.posY, color='blue', marker='o', label=None)
    
    # Plot Associations
    test = []
    for station in stationArr:
        for user in station.users:
            #all users have the same recv signal
            test.append(nodes.calculateRecievedSignalPower(station, user))
            if(nodes.calculateRecievedSignalPower(station, user) > YELLOW):
                plt.plot([user.posX, station.posX], [user.posY, station.posY], color='green', label=None)
            elif(nodes.calculateRecievedSignalPower(station, user) < YELLOW and nodes.calculateRecievedSignalPower(station, user) > RED ):
                plt.plot([user.posX, station.posX], [user.posY, station.posY], color='yellow', label=None)
            else:
                plt.plot([user.posX, station.posX], [user.posY, station.posY], color='red', label=None)

    print(f"MAX = {np.max(test)}")
    print(f"MIN = {np.min(test)}")
    
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


def getNetworkPower(stationArr):
    totalNetworkPower = 0
    time = 0
    for station in stationArr:
        print(station.state)
        ##State = multiply 0 

        time += 1
        Watts = 10**((station.transmitterPower-30)/10)
        StationPower = station.state * (Watts + (len(station.users) * 0.001))
        totalNetworkPower += StationPower
        print("Network Power at " + str(time) + " = " + str(Watts))

        print("Network Power at " + str(time) + " = " + str(StationPower))

    return totalNetworkPower
    
if __name__ == "__main__":
    GraphingPvsT(1, 1, 1)