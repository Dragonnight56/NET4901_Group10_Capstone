import gen_user_requests as usr_req
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import matplotlib.pyplot as plt
import numpy as np

def main():
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

if __name__ == "__main__":
    main()