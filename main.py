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
    plane = nodes.Plane(height=100, width=100)
    
    # Generating New Stations
    stationArr = [nodes.Station(1, posX=25, posY=25, range=20),
                  nodes.Station(2, posX=50, posY=50, range=50),
                  nodes.Station(3, posX=75, posY=75, range=20)
                  ]
    
    # Generating New Users
    userArr = [nodes.User(1, posX=20, posY=25),
               nodes.User(2, posX=40, posY=50),
               nodes.User(3, posX=60, posY=70),
               nodes.User(4, posX=80, posY=80),
               nodes.User(5, posX=40, posY=65)
                ]
    
    # Create User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)
    
    # Create Traffic for all Users
    for station in stationArr:
        for user in station.users:
            user.generateTraffic(np.random.randint(1,100))
            
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
    
    '''
    # Print Traffic for a specific Station
    for user in stationArr[0].users:
        print(f"{user.userID}: {user.traffic}")
        
    # Allocation Example
    for station in stationArr:
        trafficArr = []
        
        for user in station.users:
            trafficArr.append([user.userID, user.traffic])
        
        print(trafficArr)
        #rb_alloc.fill_channels(3,10,10,trafficArr)
    '''
    
    # Display the Current Grid
    graph.graphPlane(plane, stationArr)
    
    
if __name__ == "__main__":
    main()