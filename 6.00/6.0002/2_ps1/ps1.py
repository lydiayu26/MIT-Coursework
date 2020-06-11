################################################################################
## 6.0002 Fall 2018
## Problem Set 1
## Written By: habadio, mkebede
## Name: Lydia Yu
## Collaborators: Elena Gonzalez, Wilson Spearman
## Time: 8 hours


# Problem 1
class State():
    """
    A class representing the election results for a given state. 
    Assumes there are no ties between dem and gop votes. The party with a 
    majority of votes receives all the Electoral College (EC) votes for 
    the given state.
    """
    def __init__(self, name, dem, gop, ec):
        """
        Parameters:
        name - the 2 letter abbreviation of a state
        dem - number of Democrat votes cast
        gop - number of Republican votes cast
        ec - number of EC votes a state has 

        Attributes:
        self.name - str, the 2 letter abbreviation of a state
        self.winner - str, the winner of the state, "dem" or "gop"
        self.margin - int, difference in votes cast between the two parties, a positive number
        self.ec - int, number of EC votes a state has
        """
        self.name = name
        if dem > gop:
            self.winner = "dem"
        else:
            self.winner = "gop"
        self.margin = abs(dem-gop)
        self.ec = ec

    def get_name(self):
        """
        Returns:
        str, the 2 letter abbreviation of the state  
        """
        return self.name

    def get_ecvotes(self):
        """
        Returns:
        int, the number of EC votes the state has 
        """
        return self.ec

    def get_margin(self):
        """
        Returns: 
        int, difference in votes cast between the two parties, a positive number
        """
        return self.margin

    def get_winner(self):
        """
        Returns:
        str, the winner of the state, "dem" or "gop"
        """
        return self.winner 

    def __str__(self):
        """
        Returns:
        str, representation of this state in the following format,
        "In <state>, <ec> EC votes were won by <winner> by a <margin> vote margin."
        """
        return ("In " + self.name + ", " + str(self.ec) + "EC votes were won by " + self.winner + "by a " + str(self.margin) + "vote margin.")
        
    def __eq__(self, other):
        """
        Determines if two State instances are the same.
        They are the same if they have the same state name, winner, margin and ec votes
        Note: Allows you to check if State_1 == State_2

        Param:
        other - State object to compare against  

        Returns:
        bool, True if the two states are the same, False otherwise
        """
        if self.name == other.name and self.winner == other.winner and self.margin == other.margin and self.ec == other.ec:
            return True
        return False


# Problem 2
def load_election_results(filename):
    """
    Reads the contents of a file, with data given in the following tab-delimited format,
    State   Democrat_votes    Republican_votes    EC_votes 

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a list of State instances
    """
    results = []
    f = open(filename, 'r')
    #reads first line - skips it so you don't loop through it later
    f.readline()
    
    #loops through rest of file, creates array of str from each line, appends State object created from each element of the array to results
    for line in f:
        info = line.split()
        s = State(info[0], int(info[1]), int(info[2]), int(info[3]))
        results.append(s)
        
    return results

# Problem 3
def find_winner(election):
    """
    Finds the winner of the election based on who has the most amount of EC votes.
    Note: In this simplified representation, all of EC votes from a state go
    to the party with the majority vote.

    Parameters:
    election - a list of State instances 

    Returns:
    a tuple, (winner, loser) of the election i.e. ('dem', 'gop') if Democrats won, else ('gop', 'dem')
    """
    d = 0
    g = 0
    
    #iterates through election; adds votes from winning party to d or g
    for state in election:
        if state.get_winner() == "dem":
            d += 1 + state.get_ecvotes()
        else:
            g += 1 + state.get_ecvotes()
    
    #returns tuple based on which party has more votes        
    if d > g:
        return ("dem", "gop")
    else:
        return ("gop", "dem")
 
def states_lost(election):
    """
    Finds the list of States that were lost by the losing candidate (states won by the winning candidate).
    
    Parameters:
    election - a list of State instances 

    Returns:
    A list of State instances lost by the loser (won by the winner)
    """
    lost = []
    
    #if dem won (gop lost), add states where dem was winner (gop lost)
    if find_winner(election) == ("dem", "gop"):
        for state in election:
            if state.get_winner() == "dem":
                lost.append(state)
    
    #if gop won, add states where gop was winner            
    else:
        for state in election:
            if state.get_winner() == "gop":
                lost.append(state)
                
    return lost
        

def ec_votes_reqd(election, total=538):
    """
    Finds the number of additional EC votes required by the loser to change election outcome.
    Note: A party wins when they earn half the total number of EC votes plus 1.

    Parameters:
    election - a list of State instances 
    total - total possible number of EC votes

    Returns:
    int, number of additional EC votes required by the loser to change the election outcome
    """
    #total number of ec votes won by loser
    votes = 0
    
    #gets list of states that loser lost
    loststates = states_lost(election)
    
    #finds states that loser won and adds ec votes to votes
    for state in election:
        if state not in loststates:
            votes += state.get_ecvotes()
        
    #difference between votes needed to win and votes obtained   
    return (total/2 + 1) - votes
                                         
# Problem 4
def greedy_election(lost_states, ec_votes_needed):
    """
    Finds a subset of lost_states that would change an election outcome if
    voters moved into those states. First chooses the states with the smallest 
    win margin, i.e. state that was won by the smallest difference in number of voters. 
    Continues to choose other states up until it meets or exceeds the ec_votes_needed. 
    Should only return states that were originally lost by the loser (won by the winner) in the election.

    Parameters:
    lost_states - a list of State instances that were lost by the loser of the election
    ec_votes_needed - int, number of EC votes needed to change the election outcome
    
    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states (also can be referred to as our swing states)
    The empty list, if no possible swing states
    """
    swings = []
    
   #sorts array of lost states based on margins
    lostmargins_sorted = sorted(lost_states, key = lambda x: x.get_margin())
    
    ec_votes = 0
    i = 0
    while ec_votes < ec_votes_needed and i<len(lostmargins_sorted):
        ec_votes += lostmargins_sorted[i].get_ecvotes()
        swings.append(lostmargins_sorted[i])
        i += 1
        
    return swings

# Problem 5
def dp_move_max_voters(lost_states, ec_votes, memo=None):
    """
    Finds the largest number of voters needed to relocate to get at most ec_votes
    for the election loser. Analogy to the knapsack problem:
    Given a list of states each with a weight(#ec_votes) and value(#margin),
    determine the states to include in a collection so the total weight(#ec_votes)
    is less than or equal to the given limit(ec_votes) and the total value(#voters displaced)
    is as large as possible.

    Parameters:
    lost_states - a list of State instances that were lost by the loser 
    ec_votes - int, the maximum number of EC votes 
    memo - dictionary, an OPTIONAL parameter for memoization (don't delete!).
    Note: If you decide to use the memo make sure to override the default value when it's first called.

    Returns:
    A list of State instances such that the maximum number of voters need to be relocated
    to these states in order to get at most ec_votes 
    The empty list, if no possible states
    """
    #value is state's margin - we want to maximize value
    #weight is state's # of ecvotes - we want this to be <= ec_votes (max num ec_votes needed to change outcome)
    #takes list of states that loser lost, returns states whose ec votes are NOT needed to win election    
    #ec_votes - want to stay below that; not enough ec_votes in the end
    
    if memo == None:
        memo = {}
    #if key is already in memo, take list associated with that key in memo
    if (len(lost_states), ec_votes) in memo:
        result = memo[(len(lost_states), ec_votes)]
    #base case
    elif len(lost_states) == 0 or ec_votes == 0:
        result = tuple()
    #if the ecvotes from first element of lost_states already exceeds max ec votes needed, don't even consider it
    elif lost_states[0].get_ecvotes() > ec_votes:
        #Explore right branch only
        result = dp_move_max_voters(lost_states[1:], ec_votes, memo)
    else:
        #start with first element of lost_states; go in to left branch
        nextItem = lost_states[0]
        #Explore left branch
        withBranch =\
                 dp_move_max_voters(lost_states[1:],
                            ec_votes - nextItem.get_ecvotes(), memo)
        withVal = nextItem.get_margin()
        #sum all the margins in the list of states with the branch you are looking at
        for state in withBranch:
            withVal += state.get_margin()
       
        #Explore right branch
        withoutBranch = dp_move_max_voters(lost_states[1:],
                                                ec_votes, memo)
        withoutVal = 0
        for state in withoutBranch:
            withoutVal += state.get_margin()
        
        #Choose better branch - if withVal is better than withoutVal (withVal has greater total margins), set result equal to list withBranch with nextItem 
        if withVal > withoutVal:
            result = withBranch + (nextItem,)
        else:
            result = withoutBranch
   
    #add new entry in dictionary with result as value
    memo[(len(lost_states), ec_votes)] = result
    return result
    
def move_min_voters(lost_states, ec_votes_needed):
    """
    Finds a subset of lost_states that would change an election outcome if
    voters moved into those states. Should minimize the number of voters being relocated. 
    Only return states that were originally lost by the loser (won by the winner)
    of the election.
    Hint: This problem is simply the complement of dp_move_max_voters

    Parameters:
    lost_states - a list of State instances that the loser of the election lost
    ec_votes_needed - int, number of EC votes needed to change the election outcome

    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states (also can be referred to as our swing states)
    The empty list, if no possible swing states
    """
    #find sum of total ec votes that were lost
    totallostvotes = 0
    for state in lost_states:
        totallostvotes += state.get_ecvotes()
   
    #the lost votes you don't need to flip result is total votes you lost - votes you NNED in order to flip election    
    lostvotesnotneeded = totallostvotes - ec_votes_needed
    
    totalloststates = lost_states[:]
    
    #get list of states that you don't need in order to flip election
    notneeded = list(dp_move_max_voters(lost_states, lostvotesnotneeded))
    
    #take out the states you don't need from the total lost states
    for state in notneeded:
        totalloststates.remove(state)
        
    return totalloststates
    
    

#Problem 6
def flip_election(election, swing_states):
    """
    Finds a way to shuffle voters in order to flip an election outcome. 
    Moves voters from states that were won by the losing candidate (any state not in lost_states), 
    to each of the states in swing_states. To win a swing state, must move (margin + 1) new voters into that state. 
    Also finds the number of EC votes gained by this rearrangement, as well as the minimum number of 
    voters that need to be moved.

    Parameters:
    election - a list of State instances representing the election 
    swing_states - a list of State instances where people need to move to flip the election outcome 
                   (result of move_min_voters or greedy_election)
    
    Return:
    A tuple that has 3 elements in the following order:
        - a dictionary with the following (key, value) mapping: 
            - Key: a 2 element tuple, (from_state, to_state), the 2 letter abbreviation of the State 
            - Value: int, number of people that are being moved 
        - an int, the total number of EC votes gained by moving the voters 
        - an int, the total number of voters moved 
    None, if it is not possible to sway the election
    """
    #get states that loser won by removing states that they lost
    lost_states = states_lost(election)
    stateswon = election[:]
    for state in lost_states:
        stateswon.remove(state)
    
    #look at states with highest margin    
    sortedstateswon = sorted(stateswon, reverse = True, key = lambda x: x.get_margin())
    
    states_moved = {}
    totalecvotesgained = 0
    totalvotersmoved = 0
    statesalreadyfilled = []
    
    #goes through each state in sorted states won, gets margin and name
    for state in sortedstateswon:
        votes = state.get_margin()
        name = state.get_name()
       
        #goes through states in swing states that need voters to change election, gets num votes needed and name
        for stateto in swing_states:
            votesneeded = stateto.get_margin() + 1
            statetoname = stateto.get_name()
            
            #if state has not already been taken care of and there are enough available votes from the state won
            if stateto not in statesalreadyfilled and votes > votesneeded:
                #add stateto to list of filled states and remove the votes it needed from the available votes from won state
                statesalreadyfilled.append(stateto)
                votes -= votesneeded
                
                states_moved[(name, statetoname)] = votesneeded
                totalvotersmoved += votesneeded
                totalecvotesgained += stateto.get_ecvotes()
    
    #there were not enough available votes to fill all the states in swing states            
    if len(statesalreadyfilled) != len(swing_states):
        return None
    return (states_moved, totalecvotesgained, totalvotersmoved)

if __name__ == "__main__":
    pass
    # Uncomment the following lines to test each of the problems

    # # tests Problem 1 and Problem 2 
    # election2012 = load_election_results("2012_results.txt")

    # # tests Problem 3  
    # winner, loser = find_winner(election2012)
    # lost_states = states_lost(election2012)
    # names_lost_states = [state.get_name() for state in lost_states]
    # ec_votes_needed = ec_votes_reqd(election2012)
    # print("Winner:", winner, "\nLoser:", loser)
    # print("EC votes needed:",ec_votes_needed)
    # print("States lost by the loser: ", names_lost_states, "\n")

    # tests Problem 4
    # print("greedy_election")
    # greedy_swing = greedy_election(lost_states, ec_votes_needed)
    # names_greedy_swing = [state.get_name() for state in greedy_swing]
    # voters_greedy = sum([state.get_margin()+1 for state in greedy_swing])
    # ecvotes_greedy = sum([state.get_ecvotes() for state in greedy_swing])
    # print("Greedy swing states results:", names_greedy_swing)
    # print("Greedy voters displaced:", voters_greedy, "for a total of", ecvotes_greedy, "Electoral College votes.", "\n")

    # # tests Problem 5: dp_move_max_voters
    # print("dp_move_max_voters")
    # total_lost = sum(state.get_ecvotes() for state in lost_states)
    # move_max = dp_move_max_voters(lost_states, total_lost-ec_votes_needed)
    # max_states_names = [state.get_name() for state in move_max]
    # max_voters_displaced = sum([state.get_margin()+1 for state in move_max])
    # max_ec_votes = sum([state.get_ecvotes() for state in move_max])
    # print("States with the largest margins:", max_states_names)
    # print("Max voters displaced:", max_voters_displaced, "for a total of", max_ec_votes, "Electoral College votes.", "\n")

    # # tests Problem 5: move_min_voters
    # print("move_min_voters")
    # swing_states = move_min_voters(lost_states, ec_votes_needed)
    # swing_state_names = [state.get_name() for state in swing_states]
    # min_voters = sum([state.get_margin()+1 for state in swing_states])
    # swing_ec_votes = sum([state.get_ecvotes() for state in swing_states])
    # print("Complementary knapsack swing states results:", swing_state_names)
    # print("Min voters displaced:", min_voters, "for a total of", swing_ec_votes, "Electoral College votes. \n")