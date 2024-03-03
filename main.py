import gen_user_requests as usr_req
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import nodes
import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
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
    '''
    
    # Generating a New Plane
    plane = nodes.Plane(height=100, width=100)
    
    # Generating a New Stations
    stationArr = [nodes.Station(1, posX=50, posY=50, range=50),
                  nodes.Station(2, posX=30, posY=30, range=25),
                  nodes.Station(3, posX=70, posY=70, range=25)]
    
    # Generating a New Users
    userArr = [nodes.User(1, posX=45, posY=45),
               nodes.User(2, posX=65, posY=80),
               nodes.User(3, posX=15, posY=30),
               nodes.User(4, posX=20, posY=30)]
    
    # Create Associations
    for user in userArr:
        user.reCalculateAssociation(stationArr)
    
    # Display the Current Grid
    graph.graphPlane(plane, stationArr, userArr)
    
    
if __name__ == "__main__":
    main()