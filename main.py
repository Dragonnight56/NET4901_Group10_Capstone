import gen_user_requests as usr_req
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Example calculating transmission power
    print(cal.calc_transmit_power())

    # Example calculate data rate
    print(cal.calc_data_rate())

    # Example of Generating User Traffic
    arr = usr_req.generateTraffic(maxUsers=10, maxDataSize=256, trafficStyle=3, totalrequests=100, dataRange=12)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()