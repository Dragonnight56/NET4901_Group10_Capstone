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
    '''
    
    # Generating a New Plane
    plane = nodes.Plane(height=1000, width=1000)
    
    # Generating New Stations
    stationArr = [nodes.Station(1, posX=500, posY=300, range=50),
                  nodes.Station(2, posX=500, posY=500, range=500),
                  nodes.Station(3, posX=750, posY=750, range=50),
                  nodes.Station(4, posX=250, posY=750, range=50),
                  nodes.Station(5, posX=400, posY=400, range=50),
                  ]
    
    # Generating New Users
    userArr = nodes.generateUsers(plane, numberOfUsers=12, speed=2)
    
    # Create User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)
    
    # Create Traffic for all Users
    for station in stationArr:
        for user in station.users:
            # Each User is Given a Random Seed
            user.generateTraffic(np.random.randint(1,65536))
    
    
    # Run Simulation
    graph.statSimulation(plane, stationArr, userArr, runTime=7200)
    
    '''     
    # Pull User IDs and Traffic from all Stations
    userTraffic = []
    for station in stationArr:
        for user in station.users:
            userTraffic.append([user.userID, user.traffic])

    # Print All Current Traffic
    for user in userTraffic:
        print(f"User {user[0]}: ")
        for req in user[1]:
            print(req, end="\t")
        print()
    
    # Print Traffic for a specific Station
    for user in stationArr[0].users:
        print(f"{user.userID}: {user.traffic}")
        
    # Allocation Example
    for station in stationArr:
        trafficArr = []
        
        for user in station.users:1
            trafficArr.append([user.userID, user.traffic])
        
        print(trafficArr)
        rb_alloc.fill_channels(3,10,10,trafficArr)
    '''
    
    # Display the Current Grid
    # graph.graphPlane(plane, stationArr)
    
    
if __name__ == "__main__":
    main()