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
                userID=1
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
                userID=1
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
                userID=1
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
                userID=1
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