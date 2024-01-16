import gen_user_requests as usr_req
import matplotlib.pyplot as plt
import numpy as np

# graphing power vs time
def GraphingPvsT(time, power, dataReq):
    # Time Frame to Graph in sec (1 sec, 60 sec, 3600 sec, etc.)
    # Power in Watts over 1 sec time frames
    # Required Data Rate over 1 sec time frame
    
    # Temp Stuff
    time = 60
    arr = usr_req.generateTraffic(maxDataSize=256, trafficStyle=3, dataRange=12, totalrequests=60)

    # Power
    power = [t[1] for t in arr]
    newNum = 0
    newArr = []
    
    for i in range(len(power)):
        if i%5 == 0:
            newNum = power[i]
        newArr.append(newNum)
            
    # Plotting
    plt.bar(np.arange(1, time+1), newArr)
    plt.plot(np.arange(1, time+1), power, color='red')
    plt.show()
    
    
    pass

if __name__ == "__main__":
    GraphingPvsT(1, 1, 1)