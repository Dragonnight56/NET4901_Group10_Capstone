def round_robin(resource_element_total, resource_element_size, users_data_req):
    """
    By Jacky Liang

    Function to simulate a round robin resource allocation algorithm based purely on numeric data requirements.

    Does not handle filling the resource grid (block).
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