#########################
## EXAMPLE: returning a tuple
#########################
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

#(quot, rem) = quotient_and_remainder(4,5)
#print(quot)
#print(rem)

##########################
### EXAMPLE: various tuple operations
##########################
#seq = (2, 'a', 4, (1, 2))
#print(len(seq))
#print(seq[2] + 1)
#print(seq[3])
#i = 2
#print(seq[i - 1])
#print(seq[-1])
##print(seq[4])

#print(seq[1])
#print(seq[:-1])
#print(seq[1:3])

#for e in seq:
#    print(e)

#L = [1,2,3,4]
#for i in range(len(L)):
#    L.append(i)
#print(i)

##########################
### EXAMPLE: various list operations
### put print(L) at different locations to see how it gets mutated
##########################
#L1 = [2,1,3]
#L2 = [4,5,6]
#L3 = L1 + L2
#L1.extend([0,6])

#L = [2,1,3,6,3,7,0]
#L.remove(2)
#L.remove(3)
#del(L[1])
#print(L.pop())

#s = "I<3 cs"
#print(list(s))
#print(s.split('<'))
#L = ['a', 'b', 'c']
#print(''.join(L))
#print('_'.join(L))

#L=[9,6,0,3]
#print(sorted(L))
#L.sort()
#L.reverse()

#L = [2,1,3,6,3,7,0] 
#L.pop(5)
#print(L)
#L.remove(3)
#print(L)
#L.pop()
#print(L)

#L = [1,2,3,4]
#i = 0
#for e in L:
#    L.append(i)
#    i += 1
#print(L)

#L = [1,2,3,4]
#i = 0
#for e in L:
#    L = L + L
#    i += 1
#print(L)

##########################
### EXAMPLE: aliasing
##########################
#a = 1
#b = a
#print(a)
#print(b)
#
#warm = ['red', 'yellow', 'orange']
#hot = warm
#hot.append('pink')
#print(hot)
#print(warm)
#
##########################
### EXAMPLE: cloning
##########################
#cool = ['blue', 'green', 'grey']
#chill = cool[:]
#chill.append('black')
#print(chill)
#print(cool)
#
##########################
### EXAMPLE: sorting with/without mutation
##########################
#warm = ['red', 'yellow', 'orange']
#sortedwarm = warm.sort()
#print(warm)
#print(sortedwarm)
#
#cool = ['grey', 'green', 'blue']
#sortedcool = sorted(cool)
#print(cool)
#print(sortedcool)
#
##########################
### EXAMPLE: lists of lists of lists...
##########################
#warm = ['yellow', 'orange']
#hot = ['red']
#brightcolors = [warm]
#brightcolors.append(hot)
#print(brightcolors)
#hot.append('pink')
#print(hot)
#print(brightcolors)

################################
### EXAMPLE: mutating a list while iterating over it
################################
#def remove_dups(L1, L2):
#    for e in L1:
#        if e in L2:
#            L1.remove(e)
#
#L1 = [1, 2, 3, 4]
#L2 = [1, 2, 5, 6]
#remove_dups(L1, L2)
#print(L1)

################################
### EXERCISE: Test yourself by predicting what the output is and 
###           what gets mutated then check with the Python Tutor
################################
#cool = ['blue', 'green']
#warm = ['red', 'yellow', 'orange']
#print(cool)
#print(warm)
#
#colors1 = [cool]
#print(colors1)
#colors1.append(warm)
#print('colors1 = ', colors1)
#
#colors2 = [['blue', 'green'],
#          ['red', 'yellow', 'orange']]
#print('colors2 =', colors2)
#
#warm.remove('red') 
#print('colors1 = ', colors1)
#print('colors2 =', colors2)
#
#for e in colors1:
#    print('e =', e)
#
#for e in colors1:
#    if type(e) == list:
#        for e1 in e:
#            print(e1)
#    else:
#        print(e)
#
#flat = cool + warm
#print('flat =', flat)
#
#print(flat.sort())
#print('flat =', flat)
#
#new_flat = sorted(flat, reverse = True)
#print('flat =', flat)
#print('new_flat =', new_flat)
#
#cool[1] = 'black'
#print(cool)
#print(colors1)


#######################################
## EXAMPLE: iterative and recursive version of multiply
#######################################
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# multiply two numbers only works for some values of x, y
def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b-1)

#print(mult_iter(3,4))
#print(mult_recur(3,4))

#######################################
## EXAMPLE: iterative and recursive version of factorial
#######################################
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recur(n-1)
        
def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

#print(factorial_iter(4))
#print(factorial_recur(4))

#######################################
## EXAMPLE: multiply elements of a list 
## What happens when L = []?
#######################################
def mult_list_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0]*mult_list_recur(L[1:])

#print(mult_list_recur([2,4,6]))
        
#######################################
## EXAMPLE: find element in an ordered list
#######################################
def find_elem_recur(e, L):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return find_elem_recur(e, L[:half])
        else:
            return find_elem_recur(e, L[half:])

#L = [1,2,3,5,6,7,8]
#print(L)
#print(find_elem_recur(4, L))

#######################################
## EXAMPLE: fibonacci
#######################################
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
