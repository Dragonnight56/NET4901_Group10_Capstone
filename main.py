import gen_user_requests as usr_req
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Example calculating transmission power
    data_rate = 100  # replace with the actual value
    bandwidth = 10  # replace with the actual value
    constant_W = 2  # replace with the actual value
    power_density_noise = 0.01  # replace with the actual value
    constant_h = 3  # replace with the actual value

    # result = cal.calculate_transmitted_power(data_rate, bandwidth, constant_W, power_density_noise, constant_h)
    # print( result)

    # Example of Generating User Traffic
    arr = usr_req.generateTraffic(maxUsers=10, maxDataSize=256, trafficStyle=3, totalrequests=100, dataRange=12)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()