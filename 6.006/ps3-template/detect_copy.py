def detect_copy(D, Q):
    '''
    Input:  D | an ASCII string 
    Output: Q | an ASCII string where |Q| < |D|
    '''
    p = 2**31 - 1
    
    QVal = compute_RPrime(Q)
    currR = compute_RPrime(D[0:len(Q)])
    for i in range(0, len(D)-len(Q)):
        if currR == QVal:
            #check if actual strings are the same
            numSame = 0
            for j in range(len(Q)):
                if Q[j] == D[i+j]:
                    numSame += 1
            if numSame == len(Q):
                return True
            else:
                currR = get_next_R(D, Q, i, currR)
        else:
            currR = get_next_R(D, Q, i, currR)
    return False

def compute_RPrime(S, p=2**31 - 1):
    R_S = 0
    for i in range(len(S)):
        R_S += ord(S[i]) * 128**(len(S)-1-i)
    return R_S%p

def get_next_R(D, Q, idx, currR, p=2**31 - 1):
    f = 128**(len(Q)-1)
    #currR = compute_RPrime(D[idx:idx+len(Q)])
    firstDig = (ord(D[idx])*f)%p
    newDig = ord(D[len(Q)+idx])%p
    
    return (128*(currR-firstDig) + newDig)%p