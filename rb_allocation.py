def round_robin(channels, symbols, resource_element_size, users_data_req):
    """
    By Joshua Smith and Jacky Liang and Shub
    Function to simulate a round robin resource allocation algorithm

    Create a 2D array to simulate our resource blocks

           |     ------- Time Slot (0.5ms) = # Symbols seperated by commas ---------
    # Channels  [0,0,0,0,0,0,0,0,0,0]
           |    [0,0,0,0,0,0,0,0,0,0]
           |    [0,0,0,0,0,0,0,0,0,0]

    Assign user 1 to channel 1 (array 0)
    Assign user 2 to channel 2 (array 1)
    Assign user 3 to channel 3 (array 2)

    """
    arr = [[0 for i in range(symbols)] for j in range(channels)]
    queue = {}

    user_list = list(users_data_req)

    for user in user_list:
        i = 0
        print("USER "+ str(user[0]) + " found")
        data = user[1]

        ##While user 1 still has data, assign to channel 1
        if int(user[0]) > channels:
            queue[user[0]] = data
        else:
            while data > 0:
                if(i > 9):
                    print("Resource blocks full, queue extra data")
                    queue[user[0]] = data
                    break
                else:
                    arr[int(user[0])-1][i] = int(user[0])
                    data = data - resource_element_size
                    i = i + 1
                    
        
    for row in arr:
        print(row)
    print("This amount of data is left in the queue: " + str(queue))

    """
    ##Loop 3 times for each user, start with user 1 go to 2 and 3
    ##Loop 3 times for each user, start with user 1 go to 2 and 3
    for users, data in users_data_req.items():
        i = 0
        print("USER "+ users + " found")
        ##While user 1 still has data, assign to channel 1
        if int(users) > channels:
            queue[users] = data
        else:
            while data > 0:
                if(i > 9):
                    print("Resource blocks full, queue extra data")
                    queue[users] = data
                    break
                else:
                    arr[int(users)-1][i] = int(users)
                    data = data - resource_element_size
                    i = i + 1

    for row in arr:
        print(row)
    print("This amount of data is left in the queue: " + str(queue))

    ##process_rb.process_rblock(arr, queue)
    """
    return(arr)

# green algo( resource allocation)
def Green(channel_size, resource_element_size, users_data_req):
    cols = 10
    arr = [[0 for i in range(cols)] for j in range(channel_size)]
    print(arr)
    queue = []
    data_req = users_data_req
    for users, data in users_data_req.items():
        i = 0
        k = 0
        while True:
            print(data)

            if users == "1":
                print("USER 1 found")
                arr[k][i] = 1
                i = i + 1
                data = users_data_req["1"]
                data = data - resource_element_size
                data_req["1"] = data
                int_user = int(users)
                int_user = int_user + 1
                users = str(int_user)
                print(arr)

            elif users == "2":
                print("USER 2 found")
                arr[k][i] = 2
                i = i + 1
                data = users_data_req["2"]
                data = data - resource_element_size
                data_req["2"] = data
                int_user = int(users)
                int_user = int_user + 1
                users = str(int_user)
                print(arr)

            elif users == "3":
                print("USER 3 found")
                arr[k][i] = 3
                i = i + 1
                data = users_data_req["3"]
                data = data - resource_element_size
                data_req["3"] = data
                int_user = int(users)
                int_user = int_user - 2
                users = str(int_user)
                print(arr)

            else:
                int_user = int(users)
                int_user = int_user + 1
                users = str(int_user)
                print(users)


            if i > 9 and data > 0:
                k = k + 1
                #arr = [[0 for i in range(cols)] for j in range(channel_size)]
                i =0

    for row in arr:
        print(row)
        print("This amount of data is left in the queue: " + str(queue))
        print("Timeslots user 1 used:", User1_TS)
        print("Timeslots user 2 used:", User2_TS)
        print("Timeslots user 3 used:", User3_TS)
    return (arr)