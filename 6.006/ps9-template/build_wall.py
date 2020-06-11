def build_wall(B):
    '''
    Input:  B | a border plan corresponding to 
              | a length-5 array of length-n strings 
    Output: P | a complete non-overlapping placement for B
              | that minimizes the number of cube stones used
     c1 = []
    for i in range(len(B)):
        c1.append(B[0][i])
    c2 = []
    for i in range(len(B)):
        c2.append(B[1][i])
    '''
    P = []
    
    columns = [] #convert B into a list of strings where the strings are each column in B
    for i in range(len(B[0])):
        col = []
        for j in range(len(B)):
            col.append(B[j][i])
        columns.append(col)
    memos = dict()
    numBlocks, P = x(columns, 0, memos)

    return P

   
def x(c, i, memos):
    memoKey = "".join(letter for row in c for letter in row)
    
    if memoKey in memos:
        return memos[memoKey]
    
    lastCol = len(c)-1
    try:
        firstFree = c[i].index(".")
    except:
        if i == lastCol: #base case
            return (0, [])
        return x(c, i+1, memos)
        
      
    c[i][firstFree] = "b"
    blocks1 = x(c, i, memos)
    blocks1 = (blocks1[0] + 1, blocks1[1] + [(i, firstFree, "1")]) #min num blocks if you place 1x1
    c[i][firstFree] = "."
    

    blocksR = (float("inf"), None)
    if i < lastCol and c[i+1][firstFree] == ".": #check that c1 and c2 have the same index free
        c[i][firstFree] = "b"
        c[i+1][firstFree] = "b"
        blocksR = x(c, i, memos)
        blocksR = (blocksR[0], blocksR[1] + [(i, firstFree, "R")]) #min num blocks if you place 2x1 right
        c[i][firstFree] = "."
        c[i+1][firstFree] = "."
    
    blocksD = (float("inf"), None)
    if firstFree < len(c[i]) -1 and c[i][firstFree + 1] == ".": #make sure that there are 2 adjacent spaces free in c1
        c[i][firstFree] = "b"
        c[i][firstFree+1] = "b"
        blocksD = x(c, i, memos)
        blocksD = (blocksD[0], blocksD[1] + [(i, firstFree, "D")]) #min num blocks if you place 2x1 down
        c[i][firstFree] = "."
        c[i][firstFree+1] = "."
    
    numBlocks = min(blocks1, blocksR, blocksD, key=lambda x: x[0])
    memos[memoKey] = numBlocks
    
    return numBlocks


#def f(column): #return index of first empty cell in column c
    #for i in range(len(column)):
     #   if column[i] == ".":
      #      return i
    #return -1

#def placeBlock(column,j): #change c so that cell at index j is "b"
 #   column[j] = "b"
  #  return column