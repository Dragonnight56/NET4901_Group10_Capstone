import graphs as graph
import matplotlib.pyplot as plt
import nodes
import numpy as np
import csv

def main():

    # --- Setup Simulation ---
    # Basics
    plt.figure(figsize=(6,6))           # Defines the size of the Graph
    runTime = 7200                      # Defines how long to run the simulation in seconds
    pollingRate = 15                    # Defines how often the Simulation attempts to Reassociate Users
    updateRate = 60                     # Defines how often the AI will update the topology
    
    # Generating a New Plane
    plane = nodes.Plane(height=1000, width=1000)
    
    # Generating New Stations
        # TODO: Setup inital transmission power
    stationArr = [nodes.Station(1, posX=500, posY=500, range=500, transmitterPower=47),          # Macro Station
                  nodes.Station(2, posX=500, posY=300, range=50, transmitterPower=30),           # Pico Station
                  nodes.Station(3, posX=750, posY=750, range=50, transmitterPower=30),           # Pico Station
                  nodes.Station(4, posX=250, posY=750, range=50, transmitterPower=30),           # Pico Station
                  nodes.Station(5, posX=400, posY=400, range=50, transmitterPower=30),           # Pico Station
                  ]
    
    # Generating New Users
    userArr = nodes.generateUsers(plane, numberOfUsers=20, speed=3)
    
    # Create Initial User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)
    
    # --- End Simulation Setup ---
    
    
    
    # --- Simulation Running Loop ---

    for time in range(runTime):
        plt.clf()
        plt.xlim(0, plane.width)
        plt.ylim(0, plane.height)
        
        # Time Label
        plt.plot([],[], label=f"Time: {time}", )
        plt.legend(loc='lower right')
        
        # Update Positions
        graph.updatePositions(plane, userArr)
        
        # Replot Frame
        graph.plotFrame(stationArr, userArr)
        
        # Reassociation According to Polling Rate
        if time % pollingRate:
            nodes.calculateAssociations(userArr, stationArr)
        
        # Update Topology
        if time % updateRate:
            # Get Current State
            state = nodes.getCurrentState(stationArr)
            
            # Get AI Reccomendations
            
            # Implement AI Reccomendations
            
            # Write Current State to CSV
            
            pass
        
        # Wait a tick
        plt.pause(0.0001)
        
    plt.show()
    
    
    
    # THE LIST
    # TODO: Change this to users send signal to (interference) noise ratio (SNR / SINR) it wants the station to target
        # SNR is the received power (from station point of view)

    # TODO: Calculate loss between stations and users
    
    # TODO: Calculate stations' transmission (signal) power (P_t) needed to meet target SNR
        # P_t[dB] = target SNR[dB] + loss[dB]
        # P_t[W] = target SNR * loss
            
    # TODO: After every sim tick, save calculated values into CSV file for model training
    # https://www.freecodecamp.org/news/how-to-create-a-csv-file-in-python/
    with open('train_data.csv', 'w', newline='') as file:
        write_data = csv.writer(file)
        fields = ["Transmitted power", "Received power (signal to noise ratio)", "Station status'"]
        data_points = []

        write_data.writerow(fields)
        write_data.writerows(data_points)
       
    # TODO: Feed calculated values into DL model
    
    # TODO: Have DL model gives recommendations for which cells to turn on and off (array of 0s and 1s)
            
    # TODO: Update topology using recommendations
    
if __name__ == "__main__":
    main()