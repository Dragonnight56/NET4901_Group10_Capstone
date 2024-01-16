def round_robin(channels, symbols, resource_element_size, users_data_req):
    """
    By Joshua Smith and Jacky Liang and Shub
    Function to simulate a round robin resource allocation algorithm

    Create a 2D array to simulate our resource blocks

    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0]


    Assign user 1 to channel 1 (array 0)
    Assign user 2 to channel 2 (array 1)
    Assign user 3 to channel 3 (array 2)

    """
    arr = [[0 for i in range(symbols)] for j in range(channels)]
    print(arr)
    queue = []

    ##Loop 3 times for each user, start with user 1 go to 2 and 3
    for users, data in users_data_req.items():
        i = 0
        User1_TS = 1
        User2_TS = 1
        User3_TS = 1

        while data > 0:
            print(data)
            if users == "1":
                    print("USER 1 found")
                    arr[0][i] = 1
                    data = data - resource_element_size
                    i = i + 1

                    print(arr)

            elif users == "2":
                    print("USER 2 found")
                    arr[1][i] = 2
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)

            elif users == "3":
                    print("USER 3 found")
                    arr[2][i] = 3
                    data = data - resource_element_size
                    i = i + 1
                    print(arr)
            else:
                break

            if i > 9 and data > 0:
                if users == "1":
                    User1_TS += 1
                elif users == "2":
                    User2_TS += 1
                elif users == "3":
                    User3_TS += 1

                arr = [[0 for i in range(symbols)] for j in range(channels)]
                i = 0

    for row in arr:
        print(row)
        print("This amount of data is left in the queue: " + str(queue))
        print("Timeslots user 1 used:", User1_TS)
        print("Timeslots user 2 used:", User2_TS)
        print("Timeslots user 3 used:", User3_TS)
    return (arr)