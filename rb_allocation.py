from itertools import cycle

def channel_for_user(channels, symbols, resource_element_size, users_data_req):
    """
    By Joshua Smith, Jacky Liang, Shub B

    Function that reserves a whole channel in a resource block to transmit a user's data.
    Then allocates as many resource elements it can within the channel.
    Keep doing previous two steps until all user requests are complete.

    Example:
    2D array to simulate our resource elements in resource block
           |     ------- Time Slot (0.5ms) = # Symbols (seperated by commas) ---------
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

        # While user 1 still has data, assign to channel 1
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

    return(arr)

def fill_channels(channels, symbols, resource_element_size, users_data_req):
    # Initialize matrix with zeros
    arr = [[0 for _ in range(symbols)] for _ in range(channels)]
    # Create a copy of user data requests
    data_req = users_data_req.copy()
    # Create cyclic iterator for user keys
    cyclic_keys = cycle(users_data_req.keys())
    # Initialize user counters
    user_counters = {user_id: 0 for user_id in users_data_req}

   # while sum(data_req.values()) > 0:
    for k in range(channels):
        # Reset matrix for the first channel
        if k == 0:
            arr = [[0 for _ in range(symbols)] for _ in range(channels)]

        # Get the next user_id from cyclic iterator
        user_id = int(next(cyclic_keys))
        for i in range(symbols):
            if data_req[str(user_id)] > 0:
                print(f"USER {user_id} FOUND")
                data_req[str(user_id)] -= resource_element_size
                user_counters[str(user_id)] += 1
                print(f"Data req of {user_id}: {data_req[str(user_id)]}")
                if data_req[str(user_id)] > 0:
                    # if i > 0 :
                    arr[k][i] = user_id

            print(arr)
            print("Number of resource elements that user " + str(user_id) + " has " +  str(user_counters[str(user_id)])  )
            print("###############################################")
            # print("Current row:", k)
            # print("Current column:", i)
            # Move to the next user_id only if there are more iterations
            if i < symbols - 1:
                current_key = next(cyclic_keys)
                user_id = int(current_key)
    
    # Print the final matrix
    for row in arr:
        print(row)

    return arr