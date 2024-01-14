import matplotlib.pyplot as plt
import numpy as np


def generateTraffic(
        minUsers=1,                 # Minimum Number of Users to Generate
        maxUsers=1,                 # Maximum Number of Users to Generate
        trafficStyle=0,             # Defines the Distribution of Data      < There's a better way to do this
        minDataSize=8,              # Minimum Number of Bits to Generate
        maxDataSize=64,             # Maximum Number of Bits to Generate
        totalrequests=10,           # Number of individual requests to generate
        dataRange=12                # Fuzziness around a specific range (for linear and sin)
    ):
    """
    By Jacob Richer
    Function to generate user traffic
    Returns an Array of tuples in the form (UserID, Data, Priority)
    
    UserID is based on maxUsers
    Data is based on trafficStyle and min/maxDataSize
    Priority is randomly generated between 1 and 5
    
    ex. [(1, 128, 2) < User 1 requests 128 bits of data with priority 2
        (2, 176, 1)  < User 2 requests 176 bits of data with priority 1
        (1, 64, 3)]  < User 1 requests 64 bits of data with priority 3
    """
    # Declarations
    np.random.seed(3)
    users_data_req = []
    
    # Switch into Traffic Style
    match trafficStyle:
        # Random Style - Completely Random Generation
        case 0:
            flag = True
            if (minUsers >= maxUsers):
                UserID=1
                flag=False
                
            for i in range(1,totalrequests+1):
                
                if (flag):
                    userID = np.random.randint(minUsers, maxUsers)
                    
                if (minDataSize < maxDataSize):
                    dataRequirement = np.random.randint(minDataSize, maxDataSize)
                else:
                    dataRequirement = 0 
                
                priority = np.random.randint(1,5)
                
                users_data_req.append((userID, dataRequirement, priority))
        
        # Linear-Acending Style - Generate Traffic from min% data req to 100%
        case 1:
            scalingFactor = ((maxDataSize-dataRange)-(minDataSize+dataRange)) / (totalrequests-1)
            offset = (minDataSize+dataRange) - scalingFactor
            
            flag = True
            if (minUsers >= maxUsers):
                UserID=1
                flag=False
            
            for i in range(1,totalrequests+1):
                scalingDataSize = (scalingFactor*i) + offset
                
                if (flag):
                    userID = np.random.randint(minUsers, maxUsers)
                    
                dataRequirement = np.random.randint(scalingDataSize-dataRange, scalingDataSize+dataRange)
                if not (minDataSize <= dataRequirement <= maxDataSize):
                    dataRequirement = 0
                
                priority = np.random.randint(1,5)
                
                users_data_req.append((userID, dataRequirement, priority)) 
        
        # Linear-Descending Style - Generate Traffic from 100% to min%
        case 2:
            scalingFactor = ((minDataSize+dataRange)-(maxDataSize-dataRange)) / (totalrequests-1)
            offset = (maxDataSize-dataRange) - scalingFactor
            
            flag = True
            if (minUsers >= maxUsers):
                UserID=1
                flag=False
                
            for i in range(1,totalrequests+1):
                scalingDataSize = (scalingFactor*i) + offset
                
                if (flag):
                    userID = np.random.randint(minUsers, maxUsers)
                    
                dataRequirement = np.random.randint(scalingDataSize-dataRange, scalingDataSize+dataRange)
                if not (minDataSize <= dataRequirement <= maxDataSize):
                    dataRequirement = 0
                
                priority = np.random.randint(1,5)
                
                users_data_req.append((userID, dataRequirement, priority)) 
        
        # Sin-Wave Style - Generates a single sin wave spaning the number of elements requested at a single time
        case 3:
            amplitude = ((maxDataSize-dataRange)-(minDataSize+dataRange))/2
            frequency = (2*np.pi)/(totalrequests-1)
            vertical = amplitude + (minDataSize+dataRange)
            
            flag = True
            if (minUsers >= maxUsers):
                UserID=1
                flag=False
            
            for i in range(1,totalrequests+1):
                scalingDataSize = amplitude * np.sin(frequency * i) + vertical
                
                if (flag):
                    userID = np.random.randint(minUsers, maxUsers)
                
                dataRequirement = np.random.randint(scalingDataSize-dataRange, scalingDataSize+dataRange)
                if not (minDataSize <= dataRequirement <= maxDataSize):
                    dataRequirement = 0
                
                priority = np.random.randint(1,5)
                
                users_data_req.append((userID, dataRequirement, priority)) 
    
    # Return The Array
    return users_data_req

def round_robin(channel_size, resource_element_size, users_data_req):
    """
    By Joshua Smith and Jacky Liang and Shub
    Function to simulate a round robin resource allocation algorithm

    Create a 2D array to simulate our resource blocks

    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]


    Assign user 1 to channel 1 (array 0)
    Assign user 2 to channel 2 (array 1)
    Assign user 3 to channel 3 (array 2)

    """
    cols = 10
    arr = [[0 for i in range(cols)] for j in range(channel_size)]
    print(arr)
    queue = []

    ##Loop 3 times for each user, start with user 1 go to 2 and 3
     for users, data in users_data_req.items():
        i = 0
        User1_TS = 1
        User2_TS = 1
        User3_TS = 1

        while data > 0:
            print(data)
            if users == "1":
                    print("USER 1 found")
                    arr[0][i] = 1
                    data = data - resource_element_size
                    i = i + 1

                    print(arr)

            elif users == "2":
                    print("USER 2 found")
                    arr[1][i] = 2
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)

            elif users == "3":
                    print("USER 3 found")
                    arr[2][i] = 3
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)
            else:
                break

            if i > 9 and data > 0:
                if users == "1":
                    User1_TS += 1
                elif users == "2":
                    User2_TS += 1
                elif users == "3":
                    User3_TS += 1


                arr = [[0 for i in range(cols)] for j in range(channel_size)]
                i = 0

    for row in arr:
        print(row)
    print("This amount of data is left in the queue: " + str(queue))
    print("Timeslots user 1 used:", User1_TS)
    print("Timeslots user 2 used:", User2_TS)
    print("Timeslots user 3 used:", User3_TS)
    return (arr)

    """
    served = [False] * len(users_data_req.keys())

    while resource_element_total > 0 and False in served:
        #print(served)

        for user, data in users_data_req.items():
            if users_data_req[user] > 0:
                users_data_req[user] = data - resource_element_size
                resource_element_total -= 1

            if users_data_req[user] == 0:
                served[int(user) - 1] = True

        #print(resource_element_total)
        #print(users_data_req.items())

    return users_data_req
    """

#POWER VS TIME GRAPH CREATION CODE (I am still working on it ) - SHUB 
#############################################################################
########### 1-time slots to the multiple time slots #####################
def datarate(timeslots , req_data_amt):
    datarate = 0
    datarate = req_data_amt / timeslots
    calculate_transmitted_power(datarate)


def calculate_transmitted_power(data_rate):
        """
        Calculate transmitted power using the given formula.

        Parameters:
        - data_rate: Data rate (r)
        - bandwidth: Bandwidth (w)
        - constant_W: Constant term (W)
        - power_density_noise: Power spectral density of noise (N0)
        - constant_h: Another constant term (h)

        Returns:
        - Transmitted power (Pt)
        """
        transmitted_power = (2 ** (data_rate / bandwidth) - 1) * constant_W * power_density_noise / constant_h
        return transmitted_power
#############################################################################
########### multiple time slots to the powers time graph #########################

# timeslots is an array that carries value for each channel per time slot
# Here we will have timeslot { row = 3 (channels = 3 ) and cols = 4 (over 4 timeslots) }
Timeslots = [ [1, 1, 0, 0], [1, 0, 0, 1], [ 1, 0, 1, 0] ]

def powerConversion(array):
    global counter
    for row in array:
        if len(row) >  0:
            first_element = row[0]
            if first_element == 1:
                counter += 1
    power_per_timeslot = counter * Power_per_channel
    print(power_per_timeslot)
# graphing power vs time but here we have 1    

def GraphingPvsT():
    pass






def main():
    powerConversion(Timeslots)


if __name__ == "__main__":
    main()

