import graphs as graph
import matplotlib.pyplot as plt
import nodes
import numpy as np
import csv


def main():
    # --- Setup Simulation ---
    # Basics
    plt.figure(figsize=(7, 7))  # Defines the size of the Graph
    runTime = 7200  # Defines how long to run the simulation in seconds
    pollingRate = 15  # Defines how often the Simulation attempts to Reassociate Users
    updateRate = 60  # Defines how often the AI will update the topology
    fileName = "training_data.csv"
    totalSimPower = 0
    simPower = []
    REDLINE = -74
    YELLOWLINE = -67

    # Generating a New Plane
    plane = nodes.Plane(height=2000, width=2000)

    # Generating New Stationss
    # REMINDER  : Micro Basestation Must be the First Entry in the List
    stationArr = [nodes.Station(1, posX=1000, posY=1000, range=1200, transmitterPower=42, wavelength=0.007889, gain=7)]  # Micro Station
    exRange = nodes.calculateExRange(stationArr[0], YELLOWLINE)
    
    stationArr = stationArr + nodes.createPicoStations(plane=plane, microStation=stationArr[0], numberOfStations=10, buffer=30, exRange=exRange)

    # Generating New Users
    userArr = nodes.generateUsers(plane, numberOfUsers=50, speed=4)

    # Create Initial User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)

    totalSimPower += graph.getNetworkPower(stationArr)
    simPower.append(graph.getNetworkPower(stationArr))

    
    # Calculate Station Cell Strength vs Macro
    nodes.calculateCellStregnth(stationArr)

    # --- End Simulation Setup ---
   
   
    # --- Simulation Running Loop ---
    with open(fileName, "a", newline="") as file:
        csvWriter = csv.writer(file)
        fields = ["Time", "Minimum Signal", "Power Usage", "StationID", "Users in Range", "numberOfUsers", "signalStrength", "State"]
        csvWriter.writerow(fields)
        file.close()

        for time in range(runTime):
            plt.clf()
            plt.xlim(0, plane.width)
            plt.ylim(0, plane.height)

            # Time Label
            plt.plot([], [], label=f"Time: {time}", )
            plt.plot([], [], label=f"State: {' '.join(str(station.state) for station in stationArr)}")

            plt.legend(loc='lower right')

            # Update Positions
            graph.updatePositions(plane, userArr)

            totalSimPower += graph.getNetworkPower(stationArr)
            simPower.append(graph.getNetworkPower(stationArr))

            # Replot Frame
            graph.plotFrame(stationArr, userArr, REDLINE, YELLOWLINE)

            # Update Topology
            if not (time % updateRate):
                # Get Current State
                state = nodes.getCurrentState(stationArr, userArr, minSignal=-40, time=time)

                # Get AI Reccomendations
                suggestion = nodes.thresholdSuggestion(stationArr, userArr, 2)

                # Implement AI Reccomendations
                nodes.applySuggestions(stationArr=stationArr, stateArr=suggestion)

                # Write Current State to CSV
                with open(fileName, "a", newline="") as file:
                    csvWriter = csv.writer(file)
                    for row in state:
                        print(row)
                        csvWriter.writerow(row)
                    file.close()
                    
            # Reassociation According to Polling Rate
            if not (time % pollingRate):
                nodes.calculateAssociations(userArr, stationArr)

            # Wait a tick
            plt.pause(0.0001)
    
    
    print("TOTAL SIM POWER (W):" + str(totalSimPower))
    print(simPower)
    plt.clf()

    plt.xlim(0, runTime)
    plt.ylim(np.min(simPower)-0.025, np.max(simPower)+0.025)
    plt.plot(simPower)
    plt.xlabel("TIME")
    plt.ylabel("POWER")
    
    plt.show()
            
if __name__ == "__main__":
    main()
