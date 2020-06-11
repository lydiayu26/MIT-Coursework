###########################
#### EXAMPLE: applying functions to repeat same task many times
###########################
#A very simple example of a function that has one
#argument and returns one value
def is_even(i):   
    """Assumes: i, a positive int
    Returns True if i is even, otherwise False"""
    print("inside is_even")
    return i%2 == 0

#is_even(3) # <- returns False

# Use the is_even function later on in the code
#print("Numbers between 1 and 20: even or odd")
#for i in range(1,20):
#    if is_even(i):
#        print(i, "even")
#    else:
#        print(i, "odd")

#########################
## EXAMPLE: combinations of print and return
#########################
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

#is_even_with_return(3) 
## False

#print(is_even_with_return(3) )
## print(False)

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2
    ## return None

#is_even_without_return(3)
## None

#print(is_even_without_return(3) )
##print(None)


###########################
#### EXAMPLE: functions as arguments
###########################
def func_a():
    print('inside func_a')
    
def func_b(y):
    print('inside func_b')
    return y

def func_c(f, z):
    print('inside func_c')
    return f(z)

#print(func_a())
#print(5 + func_b(2))
#print(func_c(func_b, 3))

###########################
#### EXAMPLE: returning function objects
###########################
def f():
    def x(a, b):
        return a+b
    return x

# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
#val = f()(3,4)
#print(val)

###########################
#### EXAMPLE: shows accessing variables outside scope
###########################
def f(y):
    x = 1
    x += 1
    print(x)
    
#x = 5
#f(x)
#print(x)

def g(y):
    print(x)
    print(x+1)
    
#x = 5
#g(x)
#print(x)

def h(y):
    pass
    #x += 1 #leads to an error without line `global x` inside h

#x = 5
#h(x)
#print(x)

###########################
#### EXAMPLE: hader scope example from slides
###########################
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

#x = 3
#z = g(x)

###########################
#### EXAMPLE: complicated scope
####          Test yourself!
###########################
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

#x = 3
#z = f(x)
#print('in main program scope: z =', z)
#print('in main program scope: x =', x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    print(h(x))
    return x

#x = 3
#z = g(x)
#print('in main program scope: x = ', x)
#print('in main program scope: z = ', z)
