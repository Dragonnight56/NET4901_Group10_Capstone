import math

"""
----------------
!!! ON PAUSE !!!
----------------

"""

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
        print("USER " + str(user[0]) + " found")
        data = user[1]

        # While user 1 still has data, assign to channel 1
        if int(user[0]) > channels:
            queue[user[0]] = data
        else:
            while data > 0:
                if i > 9:
                    print("Resource blocks full, queue extra data")
                    queue[user[0]] = data
                    break
                else:
                    arr[int(user[0]) - 1][i] = int(user[0])
                    data = data - resource_element_size
                    i = i + 1

    for row in arr:
        print(row)

    print("This amount of data is left in the queue: " + str(queue))

    return arr


def fill_channels(channel_size, symbols, resource_element_size, list_of_lists):
    User_tot = {}
    for sublist in list_of_lists:
        UserNum = sublist[0]
        tuple_list = sublist[1]

        if UserNum not in User_tot:
            User_tot[UserNum] = 0

        # print(f"UserID: {UserNum}")
        # print("Data Requirement and priority:")
        for tuple_item in tuple_list:
            User_tot[UserNum] += tuple_item[0]

    for UserNum, total in User_tot.items():
        print(f"Total data requirement before processing for user  {UserNum}: {total}")

    user_traffic_dict = {user_id: total for user_id, total in User_tot.items()}

    # making an array 4 x 10
    # array = [[0] * 10 for _ in range(4)]
    # Initialize the array with the maximum possible number of rows

    max_rows = (sum(user_traffic_dict.values())) / 100  # Ceiling division to ensure we have enough rows
    round_up = math.ceil(max_rows)

    array = [[0] * 10 for _ in range(round_up)]

    users = list(user_traffic_dict.keys())
    user_index = 0

    for row in range(round_up):
        for col in range(10):
            if user_traffic_dict[users[user_index]] >= 10:
                user_traffic_dict[users[user_index]] -= resource_element_size
                array[row][col] = users[user_index]
            user_index = (user_index + 1) % len(users)

            # Check if the data requirement for all users has been met
            if sum(user_traffic_dict.values()) == 0:
                return user_traffic_dict, array
    # print(user_traffic_dict)  # printing the user and its datareq for each station as a dict

    for row in array:
        print(row)
    print(f"Total data requirement after processing for user  {UserNum}: {total}")
    return print(user_traffic_dict)


'''
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
            print("Number of resource elements that user " + str(user_id) + " has " + str(user_counters[str(user_id)]))
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
'''
