from itertools import cycle

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
    data_req = users_data_req.copy()
    cyclic_keys = cycle(users_data_req.keys())
    user_counters = {user_id: 0 for user_id in users_data_req}
    while sum(data_req.values()) > 0:
        arr = [0 for _ in range(cols) for _ in range(channel_size)]
        for k in range(channel_size):
            print("print the k = " + str(k))
            user_id = int(next(cyclic_keys))

            while data_req[str(user_id)] == 0:
                user_id = int(next(cyclic_keys))

            for i in range(cols):

             if data_req[str(user_id)] > 0:
                print(f"USER {user_id} found")
                data_req[str(user_id)] -= resource_element_size
                user_counters[str(user_id)] += 1
                print(f"Data for {user_id}: {data_req[str(user_id)]}")
                arr[k][i] = user_id

             print(arr)
             print(k)
             if i < cols - 1:
              current_key = next(cyclic_keys)
              user_id = (int(current_key))
             

    for row in arr:
        print(row)

    return arr
