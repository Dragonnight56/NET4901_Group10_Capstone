import rb_allocation as rb_alloc
import matplotlib.pyplot as plt
import numpy as np

def main():
    # TODO: Generate info about users' traffic (data) requirements
        # Name: Jacob Richer
    # TODO: Generate info about DU/RU power that are serving users
        # Name: 
    # TODO: Create another non-AI algorithm to allocate resources
        # Name: 
    # TODO: Plot a graph of data required vs time
        # Name: 
    # TODO: Plot round Robin power usage vs time
        # Name: 
    # TODO: Plot second algorithm power usage vs time
        # Name: 
    # TODO: Put all lines graphs on same figure (grid)
        # Name: 
        
    # Example usage:
    """
    data_rate = 100  # replace with the actual value
    bandwidth = 10  # replace with the actual value
    constant_W = 2  # replace with the actual value
    power_density_noise = 0.01  # replace with the actual value
    constant_h = 3  # replace with the actual value

    result = calculate_transmitted_power(data_rate, bandwidth, constant_W, power_density_noise, constant_h)
    print( result)
    """
    
    
    # Example of Round Robin 
    # print(rb_alloc.round_robin(3, 10, {"1": 50, "2": 100, "3": 250}))
    
    
    # Example of Generating User Traffic
    """
    arr = rb_alloc.generateTraffic(maxUsers=10, maxDataSize=256, trafficStyle=3, totalrequests=100, dataRange=12)
    data = [t[1] for t in arr]
    plt.scatter(np.arange(1,101), data, marker='o')
    plt.grid(True)
    plt.show()
    """
    
if __name__ == "__main__":
    main()