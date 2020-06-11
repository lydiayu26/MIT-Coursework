###################
# you can uncomment each of these examples
# and try running them yourself
###################

#today = 'Monday'
#this = "it is"
#what = this + today
#announce = this + " " + today
#silly = this + (" " + today) * 3
#print(what)
#print(announce)
#print(silly)

#number = int(input("number: "))
#if number > 0:
#    print("positive")
#    
#if number < 0:
#    print("negative")
#    
#if number == 0:
#    print("zero")
######
N = 3
for num in range(N):
    print('hello world')

#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
#if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#else:
#    print("y is smaller")
#print("thanks!")

####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right twice 
## Hint: use a counter
####################
#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while n.lower() == "right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯\n     ︵ \n    ┻━┻\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")
#
######

#n = 0
#while n < 5:
#    print(n)
#    n = n+1
#
#
####################
## EXAMPLE: for loops
####################
#for n in range(5):
#    print(n)
#
#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)
##
####################
## EXAMPLE:  fruit loops
####################
#s = "demo loops - fruit loops"
#for index in range(len(s)):
#    if s[index] == 'i' or s[index] == 'u':
#        print("There is an i or u")

######
      
#for char in s:
#    if char == 'i' or char == 'u':
#        print("There is an i or u")
#
####################
## EXAMPLE:  robot cheerleaders
####################
#an_letters = "aefhilmnorsxAEFHILMNORSX"
#
#word = input("I will cheer for you! Enter a word: ")
#times = int(input("Enthusiasm level (1-10): "))
#
#for char in word:
#    if char in an_letters:
#        print("Give me an " + char + ": " + char)
#    else:
#        print("Give me a " + char + ": " + char)
#print("What does that spell?")
#for i in range(times):
#    print(word, "!!!")   
#    
####################
## EXAMPLE: perfect squares
####################
#guess = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#while guess**2 < x:
#    guess = guess + 1
#if guess**2 == x:
#    print("Square root of", x, "is", guess)
#else:
#    print(x, "is not a perfect square")

######

#guess = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
#    neg_flag = True
#while guess**2 < x:  
#    guess = guess + 1
#if guess**2 == x: 
#    print("Square root of", x, "is", guess)
#else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")
    

####################
## EXAMPLE: perfect cubes
####################
#cube = int(input("Enter an integer: "))
#for guess in range(cube+1):
#    if guess**3 == cube:
#        print("Cube root of", cube, "is", guess)

######     

#cube = int(input("Enter an integer: "))
#for guess in range(abs(cube)+1):
#    if guess**3 == abs(cube):
#        if cube < 0:
#            guess = -guess
#        print("Cube root of " +str(cube)+" is "+str(guess))

######      

#cube = int(input("Enter an integer: "))
#for guess in range(abs(cube)+1):
#    if guess**3 >= abs(cube):
#        break
#if guess**3 != abs(cube):
#    print(cube, "is not a perfect cube")
#else:
#    if cube < 0:    
#        guess = -guess
#    print("Cube root of " +str(cube)+" is "+str(guess)) 

####################
## EXAMPLE: word problems
####################
#for alyssa in range(1001):
#    ben = max(alyssa - 20, 0)
#    cindy = alyssa * 2
#    if ben + cindy + alyssa == 1000:
#        print("Alyssa sold " + str(alyssa) + " tickets")
