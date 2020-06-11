def greedy_cow_transport(cows,limit=10):
    """
    cows: a dictionary of name (string), weight (int) pairs
    limit: weight limit of the spaceship (an int)

    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows.

    The greedy heuristic should follow the following method:
    1. As long as the current trip can fit another cow, add the lightest 
       cow that will fit to the trip
    2. Once the trip is full, begin a new trip to transport some of the remaining cows
    Does not mutate the dictionary cows.

    Returns a list of lists, with each inner list containing the names of cows
    transported on a particular trip. The list should be in the order of the trips.
    """
    # YOUR CODE HERE
    ships = []
    #a list of tuples (name, weight) sorted in order from least weight to greatest
    #sorted list allows you to add the lightest cow remaining each time
    sortedCows = sorted(cows.items(), key=lambda x: x[1])
    remainingCows = sortedCows[:]
    
    #make sure there are still cows left to look at
    while len(remainingCows) != 0:
        currentShip = []
        index = 0
        currentShipWeight = 0
        #make sure the index doesn't go out of range and the current cow being looked at doesn't make the ship exceed limit
        #keep adding cows until the ship is full
        while index < len(remainingCows) and (currentShipWeight + remainingCows[index][1]) <= limit:
            #add name of current cow to ship and its weight to currentShipWeight
            currentShipWeight += remainingCows[index][1]
            currentShip.append(remainingCows[index][0])
            index += 1
        #for next ship, only look at cows in remainingCows after the current index that was looked at
        remainingCows = remainingCows[index:]
        #add currentShip to list of ships
        ships.append(currentShip)
        
    return ships