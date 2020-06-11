
#print('10*0.1', '==', 10*0.1)
#
#x = 0
#for i in range(8):
#    x += 0.125
#print(x == 1)

#x = int(input("Enter an integer: "))
#foundAnswer = False
#for guess in range(x + 2):
#    if guess**2 == x:
#        print("Square root of", x, "is", guess)
#        foundAnswer = True
#if not foundAnswer:
#    print(x, "is not a perfect square")

#x = int(input("Enter an integer: "))
#epsilon = 0.01
#numGuesses = 0
#ans = 0.0
#increment = 0.0001
#while abs(ans**2 - x) >= epsilon:
#    ans += increment
#    numGuesses += 1
#print('numGuesses =', numGuesses)
#if abs(ans**2 - x) >= epsilon:
#    print('Failed on square root of', x)
#else:
#    print(ans, 'is close to square root of', x)

#x = 54321
#epsilon = 0.01
#numGuesses = 0
#ans = 0.0
#increment = 0.0001
#while abs(ans**2 - x) >= epsilon:
#    ans += increment
#    numGuesses += 1
#    if numGuesses%50000 == 0:
#        print('Current guess =', ans)
#        print('Current guess**2 - x =',
#                ans*ans - x)
#print('numGuesses =', numGuesses)
#if abs(ans**2 - x) >= epsilon:
#    print('Failed on square root of', x)
#else:
#    print(ans, 'is close to square root of', x)

#x = 54321
#epsilon = 0.01
#numGuesses = 0
#ans = 0.0
#increment = 0.00001
#while abs(ans**2 - x) >= epsilon and ans**2 <= x:
#    ans += increment
#    numGuesses += 1
#    if numGuesses%50000 == 0:
#        print('Current guess =', ans)
#        print('Current guess**2 - x =',
#                ans*ans - x)
#print('numGuesses =', numGuesses)
#if abs(ans**2 - x) >= epsilon:
#    print('Failed on square root of', x)
#    print('Last guess was', ans)
#    print('Last guess squared is', ans*ans)
#else:
#    print(ans, 'is close to square root of', x)

#min = 1
#max = 447
#found = False
#while not found:
#    guess = min + (max - min)//2
#    print('I guess', guess)
#    answer = input('Enter h, l, or c: ')
#    if answer == 'c':
#        print('Congratulations')
#        found = True
#    elif answer == 'h':
#        max = guess - 1
#    else:
#        min = guess + 1
#    print(min, max)

#x = 54321
#epsilon = 0.01
#numGuesses = 0
#low = 1.0
#high = x
#ans = (high + low)/2
#
#while abs(ans**2 - x) >= epsilon:
#    print('low = ' + str(low) + ' high = ' + str(high)\
#          + ' ans = ' + str(ans))
#    numGuesses += 1
#    if ans**2 < x:
#        low = ans
#    else:
#        high = ans
#    ans = (high + low)/2.0
#print('numGuesses = ' + str(numGuesses))
#print(str(ans) + ' is close to square root of ' + str(x))


