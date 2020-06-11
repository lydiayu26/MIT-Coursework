def min_mod_tuple(A, k):
    i, j = 0, 1
    minVal = (A[i] * A[j])%k
    for x in range(0,len(A)):
        for y in range(1,len(A)):
            newMinVal = (A[x]*A[y])%k
            if newMinVal < minVal:
                minVal = newMinVal
                i = x
                j = y
    return (i, j)
