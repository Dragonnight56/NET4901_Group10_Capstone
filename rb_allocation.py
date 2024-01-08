users_data_req = {"1": 50, "2": 100, "3": 250}

RB_total = 25
RB_size = 10

while RB_total > 0:
    for user, data in users_data_req.items():
        if (users_data_req[user] > 0):
            users_data_req[user] = data - RB_size
            RB_total -= 1
    
    print(RB_total)
    print(users_data_req.items())