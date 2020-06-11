def count_paths(F):
    '''
    Input:  F | size-n direct access array of size-n direct access arrays
              | each F[i][j] is either 't', 'm', or 'x'
              | for tree, mushroom, empty respectively
    Output: m | the number of distinct optimal paths in F
              | starting from (0,0) and ending at (n-1,n-1)
    '''
    p = k = dict()
    numpaths = 0
    p=findPaths(F, len(F)-1, len(F)-1, p,k, True)
    numpaths = p[(len(F)-1,len(F)-1)]
    return numpaths


def findPaths(F,i,j, p,k,initial=False):
    m = 0
    if initial:
        p = dict()
        k = dict()
    if F[i][j] == 't': #no path to square if it contains a tree
        p[(i,j)] = -1
        k[(i,j)] = -1
        return
    if F[i][j] == 'm': #check to see if there is a mushroom in square
        m += 1
    if i==0 and j==0: #starting square
        p[(i,j)] = 1
        k[(i,j)] = m
        return
    if i<0 or j<0 or i>len(F)-1 or j>len(F)-1: #make sure square is not out of bounds
        p[(i,j)] = -1
        k[(i,j)] = -1
        return
        
    if (i,j) not in p: #we don't need to recalculate values that we've already calculated
        findPaths(F, i-1, j,p,k)
        findPaths(F, i, j-1,p,k)
        
        if k[(i-1,j)] == k[(i,j-1)]: #preceding squares have same max mushrooms
            p[(i,j)] = p[(i-1,j)] + p[(i,j-1)]
            k[(i,j)] = k[(i-1,j)] + m
        elif k[(i-1,j)] > k[(i,j-1)]: #left square has higher max mushroom than top square
            p[(i,j)] = p[(i-1,j)]
            k[(i,j)] = k[(i-1,j)] + m
        else: #top square has higher max mushroom than left
            p[(i,j)] = p[(i,j-1)]
            k[(i,j)] = k[(i,j-1)] + m
    return p