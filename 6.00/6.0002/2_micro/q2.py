def getPaths(currentPath, currency_to, exchange_rates):
    #the current starting node is always equal to the last node to just added to the path
    currentStart = currentPath[-1]
    #base case: if the start and end nodes are the same, return the path
    if currentStart == currency_to:
        return [currentPath]
    #make a list of all possible currency_to starting with the start node
    connections = []
    for rate in exchange_rates:
        #look at the rates that have the start as currency_from and add that currency_to to connections
        if rate[0] == currentStart:
            connections.append(rate[1])
        #otherwise if the start is the currency_to then do the opposite
        elif rate[1] == currentStart:
            connections.append(rate[0])
    #make a list of all currency_to that are not already in the current path
    validConnections = []
    for endNode in connections:
        if endNode not in currentPath:
            validConnections.append(endNode)
    pathsFound = []
    #look at each valid currency_to
    for node in validConnections:
        #extend the currentPath by that node and add that new path to pathsFound
        newPath = getPaths(currentPath+[node], currency_to, exchange_rates)
        pathsFound.extend(newPath)
        
    return pathsFound


def exchange_money(exchange_rates, amount, currency_from, currency_to):
    """
    exchange_rates: list of lists for all exchange rates, where one exchange rate
            is represented as: [currency_from, currency_to, exchange_rate]
    exchange_rate: positive and non-zero float s.t.
            amount_of_currency_from*exchange_rate = amount_of_currency_to
            amount_of_currency_to*(1/exchange_rate) = amount_of_currency_from
    currency_from, currency_to: str
    amount: float representing the amount of money you wish to exchange
    currency_from: string representing the currency that 'amount' is in
    currency_to: string representing the currency you wish to change 'amount' to
        
    Returns a float, rounded to 2 decimal places, representing the maximum amount
    of currency_to that can be achieved by using the exchange rates in exchange_rates to  
    exchange the amount of currency_from.

    If there is no path from curency_from to currency_to, returns None
    Hint: you should utilize classes from previous problem sets.
    """
    # YOUR CODE HERE
    #get all possible paths. If none exist, return none
    paths = getPaths([currency_from], currency_to, exchange_rates)
    if len(paths) == 0:
        return None
   
    #make a list of the total rate that the amount would be multiplied by for each path
    rateForEachPath = []
    for path in paths:
        totalRate = 1
        for i in range(len(path)-1):
            #loop through exchange_rates
            for rate in exchange_rates:
                #match each pair of adjacent path nodes to their exchange rates and multiply totalRate by that rate
                if rate[0] == path[i] and rate[1] == path[i+1]:
                    totalRate *= rate[2]
                #if the nodes are switched, multiply by 1/rate
                elif rate[0] == path[i+1] and rate[1] == path[i]:
                    totalRate *= 1/rate[2]
        rateForEachPath.append(totalRate)
     
    #find maximum rate out of all the paths
    maxRate = max(rateForEachPath)
    return round(maxRate * amount, 2)
    



    