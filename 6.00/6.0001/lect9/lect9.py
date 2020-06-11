import time

def timeFunc(f, arg):
    print('Timing', f.__name__)
    for i in range(3):
        t0 = time.clock()
        f(arg)
        t1 = time.clock() - t0
        print('Wall time =', t1, 'sec.')

def centToFaren(c):
    print(c*9/5 + 32)

def count(x):
    total = 0
    for i in range(x):
        total += i
    return total

timeFunc(centToFaren, -40)
timeFunc(count, 10000000)

def power(x, e):
    """
    Assumes x a float, e a positive int
    Returns x**e
    """
    res = 1
    for i in range(e):
        res *= x
    return res

def isIn(L, e):
    for elem in L:
        if elem == e:
            return True
    return False

def fact_iter(n):
    """assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

#for i in range(n):
#      print 'a'
#  for j in range(n*n):
#      print 'b'
#
#for i in range(n):
#      for j in range(n):
#          print 'a'

def search1(L, e):
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False
    
def search2(L, e):
    """Assumes L is sort in ascending order"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
               tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
