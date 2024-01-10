import rb_allocation as rb_alloc

def main():
    # TODO: Generate info about users' traffic (data) requirements
        # Name: 
    # TODO: Generate info about DU/RU power that are serving users
        # Name: 
    # TODO: Create another non-AI algorithm to allocate resources
        # Name: 
    # TODO: Plot a graph of data required vs time
        # Name: 
    # TODO: Plot round Robin power usage vs time
        # Name: 
    # TODO: Plot second algorithm power usage vs time
        # Name: 
    # TODO: Put all lines graphs on same figure (grid)
        # Name: 

    print(rb_alloc.round_robin(100, 10, {"1": 50, "2": 100, "3": 250}))

if __name__ == "__main__":
    main()