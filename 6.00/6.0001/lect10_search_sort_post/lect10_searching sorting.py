import time
import random

####### add digits of a string
def int_to_str(n):
    """ assumes n an int >= 0 """
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer

    
####### searching on unsorted list
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

####### searching on sorted list
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

#################################
## Bisection search with copying list
#################################    
def bisect_search1(L, e):
    """
    Assumes L is a list with elements in ascending order.
    Returns True if e is in L and False otherwise
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

#################################
## Bisection search with indices
#################################    
def bisect_search2(L, e):
    """
    Assumes L is a list with elements in ascending order.
    Returns True if e is in L and False otherwise
    """
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

#print('-------')
#for i in [100,1000,10000,100000,1000000,10000000]:
#    # list comprehension 
#    # -> create a list where each element is x where x is each value in range(i)
#    L = [x for x in range(i)] 
#    e = -1
#    t0 = time.clock()
#    print(linear_search(L, e), "with linear_search", i, "took", 1000*round(time.clock() - t0, 6))
#print('-------')
#for i in [100,1000,10000,100000,1000000,10000000]:
#    # list comprehension 
#    # -> create a list where each element is x where x is each value in range(i)
#    L = [x for x in range(i)] 
#    e = -1
#    t0 = time.clock()
#    print(bisect_search1(L, e), "with bisect_search1", i, "took", 1000*round(time.clock() - t0, 6))
#print('-------')
#for i in [100,1000,10000,100000,1000000,10000000]:
#    # list comprehension 
#    # -> create a list where each element is x where x is each value in range(i)
#    L = [x for x in range(i)]
#    e = -1
#    t0 = time.clock()
#    print(bisect_search2(L, e), "with bisect_search2", i, "took", 1000*round(time.clock() - t0, 6))



############################
## Example of exponential cost
## power set computation
############################
        
def genSubsets(L):
    if len(L) == 0:
        return [[]] 
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

#test = [1,2,3,4]
#print(genSubsets(test))
    
    
    
############################
## Bogo/Random/Monkey Sort Example
############################
def is_sorted(L):
    i = 0
    j = len(L)
    while i + 1 < j:
        if L[i] > L[i + 1]:
            return False
        i += 1
    return True
 
def bogo_sort(L):
    count = 0
    while not is_sorted(L):
        random.shuffle(L)
        count += 1
    return count
# 
#print("--- BOGO SORT ---")
#L = []
#for i in range(0, 9):
#    L.append(random.randint(0, 100))
##L = [8, 4, 1, 6, 5, 11, 2, 0]
#print('L:       ', L)
#t0 = time.clock()
#count = bogo_sort(L)
#print('Sorted L:', L)
#print(count, "shuffles and sorting took: ", time.clock() - t0, " s")

############################
## Bubble Sort Example
############################
def bubble_sort(L, detail = False):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
            if detail == True:
                print(L)

#print("--- BUBBLE SORT ---")
#L = [8, 4, 1, 6, 5, 11, 2, 0]
#print('L:       ', L)
#bubble_sort(L, True)
#print('Sorted L:', L)
  

############################
## Selection Sort Example
############################
def selection_sort(L, detail = False):
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
            if detail == True:
                print(L)

#print("--- SELECTION SORT ---")
#L = [8, 4, 1, 6, 5, 11, 2, 0]
#print('L:       ', L)
#selection_sort(L, True)
#print('Sorted L:', L)


############################
## Merge Sort Example
############################
def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # one list is empty
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    
def merge_sort(L, detail = False):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        # divide
        left = merge_sort(L[:middle], detail)
        right = merge_sort(L[middle:], detail)
        if detail == True:
            print("Merging", left, "and", right)
        # conquer
        return merge(left, right)
    
#print("--- MERGE SORT ---")
#L = [8, 4, 1, 6, 5, 11, 2, 0]
#print('L:       ', L)
#print(merge_sort(L, True))
        
def quick_sort(L):
  quick_sort_help(L,0,len(L)-1)

def quick_sort_help(L,first,last):
  if first<last:
      splitpoint = partition(L,first,last)
      quick_sort_help(L,first,splitpoint-1)
      quick_sort_help(L,splitpoint+1,last)

def partition(L,first,last):
  pivotvalue = L[first]
  leftmark = first+1
  rightmark = last
  done = False
  while not done:
      while leftmark <= rightmark and L[leftmark] <= pivotvalue:
          leftmark = leftmark + 1
      while L[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1
      if rightmark < leftmark:
          done = True
      else:
          temp = L[leftmark]
          L[leftmark] = L[rightmark]
          L[rightmark] = temp
  temp = L[first]
  L[first] = L[rightmark]
  L[rightmark] = temp
  return rightmark

#print("--- QUICK SORT ---")
#L = []
#for i in range(0, 9):
#    L.append(random.randint(0, 100))
##L = [8, 4, 1, 6, 5, 11, 2, 0]
#print('L:       ', L)
#quickSort(L)
#print(L)