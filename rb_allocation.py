import matplotlib.pyplot as plt

def round_robin(channel_size, resource_element_size, users_data_req):
    """
    By Joshua Smith and Jacky Liang
    Function to simulate a round robin resource allocation algorithm

    Create a 2D array to simulate our resource blocks

    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]


    Assign user 1 to channel 1 (array 0)
    Assign user 2 to channel 2 (array 1)
    Assign user 3 to channel 3 (array 2)

    """
    cols = 10
    arr = [[0 for i in range(cols)] for j in range(channel_size)]
    print(arr)
    queue = []

    ##Loop 3 times for each user, start with user 1 go to 2 and 3
    for users, data in users_data_req.items():
        i = 0
        ##While user 1 still has data, assign to channel 1
        while data > 0:
            print(data)
            if users == "1":
                if(i > 9):
                    print("Resource blocks full, queue extra data")
                    queue = data
                    break
                else:
                    print("USER 1 found")
                    arr[0][i] = 1
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)
            elif users == "2":
                if(i > 9):
                    print("Resource blocks full, queue extra data")
                    queue = data
                    break
                else:
                    print("USER 2 found")
                    arr[1][i] = 2
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)
            elif users == "3":
                if(i > 9):
                    print("Resource blocks full, queue extra data")
                    queue = data
                    break
                else:
                    print("USER 3 found")
                    arr[2][i] = 3
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)  
            else:
                break
                
    for row in arr:
        print(row)
    print("This amount of data is left in the queue: " + str(queue))

    return(arr)

    """
    served = [False] * len(users_data_req.keys())

    while resource_element_total > 0 and False in served:
        #print(served)

        for user, data in users_data_req.items():
            if users_data_req[user] > 0:
                users_data_req[user] = data - resource_element_size
                resource_element_total -= 1

            if users_data_req[user] == 0:
                served[int(user) - 1] = True

        #print(resource_element_total)
        #print(users_data_req.items())

    return users_data_req
    """

#POWER VS TIME GRAPH CREATION CODE (I am still working on it ) - SHUB 
#############################################################################
########### 1-time slots to the multiple time slots #####################



#############################################################################
########### multiple time slots to the powers time graph #########################

# timeslots is an array that carries value for each channel per time slot
# Here we will have timeslot { row = 3 (channels = 3 ) and cols = 4 (over 4 timeslots) }
Timeslots = [ [1, 1, 0, 0], [1, 0, 0, 1], [ 1, 0, 1, 0] ]

def powerConversion(array):
    global counter
    for row in array:
        if len(row) >  0:
            first_element = row[0]
            if first_element == 1:
                counter += 1
    power_per_timeslot = counter * Power_per_channel
    print(power_per_timeslot)
# graphing power vs time but here we have 1    
def GraphingPvsT():

def main():
    powerConversion(Timeslots)


if __name__ == "__main__":
    main()

