import random

def average_streak_count(n, streak, num_trials):
    """
    n: number of coin flips in one trial
    streak: a string of length > 0, representing the sequence of 
            heads or tails in one trial. Heads represented as "H" and tails as "T"
    num_trials: number of trials in the simulation
    Runs a Monte Carlo simulation with a number of trials 'num_trials'. For each 
    trial, it tracks the number of times 'streak' occurs when a fair coin is 
    flipped 'n' times. After 'num_trials' number of trials, it returns a tuple of: 
    (1) the average number of times the streak occurs
    (2) the width of the 95% confidence interval rounded to 3 decimal places 
        (from the mean to one side, only)
    """
 
    # You are given this function - do not modify
    def get_mean_std(X):
        mean = sum(X)/len(X)
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        std = (tot/len(X))**0.5
        return (mean, std)

    # YOUR CODE HERE

    #X is list of streak counts for each trial run
    X = []
    for i in range(num_trials):
        #add the resulting count from this trial to the list
        X.append(oneTrial(n, streak))
        
    #calculate mean and std of the trials using function given
    meanStd = get_mean_std(X)
    avg = meanStd[0]
    std = meanStd[1]
    confInt = 1.96 * (std/((num_trials)**0.5))
    
    return (avg, round(confInt, 3))


def oneTrial(n, streak):
        result = ""
        #flips coin n times
        for i in range(n):
            flip = random.choice([True, False])
            #if true, add heads to result
            if flip == True:
                result += "H"
            #if false, add tails to result
            else:
                result += "T" 
        
        count = 0
        startIndex = 0
        found = True
        #while streak exists as a substring of the coin toss result string
        while found:
            #get the index of the first appearance of streak in the substring of result that begins at index startIndex
            index = result.find(streak, startIndex)
            #exit loop if streak doesn't exist in result
            if index == -1:
                found = False
            else:
                #set startIndex to the index right after the index of the 1st appearance of streak to look at the rest of the result string
                startIndex = index + 1
                #increase the occurrences of streak by 1
                count += 1
        
        return count
    
    