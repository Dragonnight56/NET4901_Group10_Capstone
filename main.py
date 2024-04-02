import graphs as graph
import matplotlib.pyplot as plt
import nodes
import numpy as np
import csv


def main():
    # --- Setup Simulation ---
    # Basics
    plt.figure(figsize=(7, 7))  # Defines the size of the Graph
    runTime = 61  # Defines how long to run the simulation in seconds
    pollingRate = 10  # Defines how often the Simulation attempts to Reassociate Users
    updateRate = 30  # Defines how often the AI will update the topology
    fileName = "training_data.csv"

    # Generating a New Plane
    plane = nodes.Plane(height=1000, width=1000)

    # Generating New Stations
    # REMINDER  : Macro Basestation Must be the First Entry in the List
    stationArr = [nodes.Station(1, posX=500, posY=500, range=750, transmitterPower=34)]  # Macro Station
    stationArr = stationArr + nodes.createPicoStations(plane, 10, buffer=20)

    # Generating New Users
    userArr = nodes.generateUsers(plane, numberOfUsers=200, speed=4)

    # Create Initial User/Station Associations
    nodes.calculateAssociations(userArr, stationArr)
    
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
            plt.legend(loc='lower right')

            # Update Positions
            graph.updatePositions(plane, userArr)

            # Replot Frame
            graph.plotFrame(stationArr, userArr)

            # Reassociation According to Polling Rate
            if not (time % pollingRate):
                nodes.calculateAssociations(userArr, stationArr)

            # Update Topology
            if not (time % updateRate):
                # Get Current State
                # Comment out atm if want to test calculate signal funcs
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

            # Wait a tick
            plt.pause(0.0001)
            
            
    
    # THE LIST
    # TODO: Simulation isn't actively writing to the CSV file, only after the simulation finishes.
    #       Not sure why, to replicate you can kill the simulation mid-runtime and check the csv file.
    
    # TODO: Feed calculated values into DL model

    # TODO: Have DL model gives recommendations for which cells to turn on and off (array of 0s and 1s)

    # TODO: Update topology using recommendations
    
    # TODO: Speed Up the Simulation
    #           - Code Refactors
    #           - Pre-Calculate Whatever is possible


if __name__ == "__main__":
    main()
