import gen_user_requests as usr_req
import nodes
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import matplotlib.pyplot as plt
import numpy as np

"""
----------------
!!! ON PAUSE !!!
----------------

"""

def main():
    # Testing Area
    # myStation = nodes.Station(1, posX=50, posY=50, range=20, transmitterGain=5, transmitterPower=25, wavelength=0.07)
    # myStation.calcMaxRange()    
    
    '''
    # First Demo, Generating User Traffic
    arr = usr_req.generateTraffic(maxUsers=3, maxDataSize=256, trafficStyle=0, totalrequests=100)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()
    
    arr = usr_req.generateTraffic(maxUsers=3, maxDataSize=256, trafficStyle=1, totalrequests=100, dataRange=12)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()
    
    arr = usr_req.generateTraffic(maxUsers=3, maxDataSize=256, trafficStyle=3, totalrequests=100, dataRange=20)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()

    # Second Demo, Joshua's algorithm
    rb_alloc.channel_for_user(3, 10, 10, arr)

    # Third Demo, Shub's algorithm
    rb_alloc.fill_channels(3,10,10,{"1":500 , "2": 100,"3":350})
    
    # Fourth Demo, Power/Time Graph
    graph.GraphingPvsT(1, 1, 1)
    '''

if __name__ == "__main__":
    main()