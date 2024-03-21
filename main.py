import gen_user_requests as usr_req
import rb_allocation as rb_alloc
import stats_calc as cal
import graphs as graph
import nodes
import matplotlib.pyplot as plt
import numpy as np

def main():

    # --- Setup Simulation ---
    # Generating a New Plane
    plane = nodes.Plane(height=1000, width=1000)
    
    # Generating New Stations
        # TODO: Setup inital transmission power
    stationArr = [nodes.Station(1, posX=500, posY=300, range=50),
                  nodes.Station(2, posX=500, posY=500, range=500),
                  nodes.Station(3, posX=750, posY=750, range=50),
                  nodes.Station(4, posX=250, posY=750, range=50),
                  nodes.Station(5, posX=400, posY=400, range=50),
                  ]
    
    # Generating New Users
    userArr = nodes.generateUsers(plane, numberOfUsers=20, speed=3)
    
    # Create Initial User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)
    
    # Create Traffic for all Users
        # TODO: Change this to users send signal to (interference) noise ratio (SNR / SINR) it wants the station to target
            # SNR is the received power (from station point of view)
    for station in stationArr:
        for user in station.users:
            # Each User is Given a Random Seed
            user.generateTraffic(np.random.randint(1,65536))

    # TODO: Calculate loss between stations and users
    
    # TODO: Calculate stations' transmission (signal) power (P_t) needed to meet target SNR
        # P_t[dB] = target SNR[dB] + loss[dB]
        # P_t[W] = target SNR * loss
            
    # TODO: After every sim tick, save calculated values into CSV file for model training
            
    # TODO: Feed calculated values into DL model
    
    # TODO: Have DL model gives recommendations for which cells to turn on and off (array of 0s and 1s)
            
    # TODO: Update topology using recommendations
    
    # Run Simulation
    graph.statSimulation(plane, stationArr, userArr, runTime=7200)
    
if __name__ == "__main__":
    main()