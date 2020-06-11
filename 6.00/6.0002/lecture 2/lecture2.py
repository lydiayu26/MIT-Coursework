class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0, 0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, metric, toPrint):
    metrics = {'value': Food.getValue,'density':Food.density,
               'cost': lambda x: 1/Food.getCost(x)}
    try:
        taken, val = greedy(items, constraint, metrics[metric])
    except:
        print('Unknown metric', metric)
        return
    if toPrint:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
    return val

def testGreedys(foods, maxUnits, toPrint = True):
    bestVal = 0
    for metric in ('value', 'density', 'cost'):
        if toPrint:
            print('Use greedy by', metric,
                  'on', len(foods), 'items')
        bestVal = max(testGreedy(foods, maxUnits, metric,
                                 toPrint), bestVal)
    return bestVal

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items,
          avail a weight
       Returns a tuple of the total value of a solution
          to the 0/1 knapsack problem and the items of
          that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ()) #0 value, nothing taken
    elif toConsider[0].getCost() > avail: #cannot afford current item
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, toPrint = True):
    val, taken = maxVal(foods, maxUnits)
    if toPrint:
        print('Optimal value =', val)
        for item in taken:
            print('   ', item)
    return val

#names = ['wine', 'beer', 'pizza', 'burger', 'fries',
#         'cola', 'apple', 'donut', 'cake']
#values = [89,90,95,100,90,79,50,10]
#calories = [123,154,258,354,365,150,95,195]
#foods = buildMenu(names, values, calories)
#
#greedyVal = testGreedys(foods, 750)
#print('')
#optVal = testMaxVal(foods, 750)
#print('\nBest greedy solution =', greedyVal,
#      '\nOptimal solution =', optVal)

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

#import random
#random.seed(1)
#
#numCalories = 750
#for numItems in (8, 16, 32, 64, 128, 256, 512, 1024):
#    items = buildLargeMenu(numItems, 100, 300)
#    print('Test on', len(items), 'items')
#    greedyVal = testGreedys(items, numCalories, False)
#    print('Best greedy solution =', greedyVal)
#    optVal = testMaxVal(items, numCalories, False)
#    print('Optimal solution =', optVal, '\n')  

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#for i in range(0, 1000, 5):
#    try:
#        print('fib(' + str(i) + ') =', fib(i))
#    except:
#        print('Failed')
#        break
        
def fastFib(n, memo = None):
    """Assumes n is an int >= 0, memo used only by
         recursive calls
       Returns Fibonacci of n"""
    if memo == None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

#import sys
#sys.setrecursionlimit(2000)
        
#for i in range(0, 1000, 5):
#    try:
#        print('fib(' + str(i) + ') =', fastFib(i))
#    except:
#        print('Failed')
#        break

#print(fastFib(970))

def fastMaxVal(toConsider, avail, memo = None):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if memo == None:
        memo = {}
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testFastMaxVal(foods, maxUnits, toPrint = True):
    val, taken = fastMaxVal(foods, maxUnits)
    if toPrint:
        print('Optimal value =', val)
        for item in taken:
            print('   ', item)
    return val

#import random
#random.seed(1)
#         
#numCalories = 750
#for numItems in (8, 16, 32, 64, 128, 256, 512, 1024):
#    items = buildLargeMenu(numItems, 100, 300)
#    print('Test on', len(items), 'items')
#    greedyVal = testGreedys(items, numCalories, False)
#    print('Best greedy solution =', greedyVal)
#    optVal = testFastMaxVal(items, numCalories, False)
#    print('Optimal solution =', optVal, '\n')

def buildLargeMenu1(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.random()*maxCost))
    return items
          
#import random
#random.seed(1)
#         
#numCalories = 750
#for numItems in (8, 16, 32, 64, 128, 256, 512, 1024):
#    items = buildLargeMenu1(numItems, 100, 300)
#    print('Test on', len(items), 'items')
#    greedyVal = testGreedys(items, numCalories, False)
#    print('Best greedy solution =', greedyVal)
#    optVal = testFastMaxVal(items, numCalories, False)
#    print('Optimal solution =', optVal, '\n')

#e1 if c else e2
#x/y if y !=0 else None

#L = [x*x for x in range(10)]
#print(L)
#
#L = []
#for i in range(10):
#    L.append(i*i)
#print(L)
#
#L = [i**2 for i in range(10) if i%2 != 0]
#print(L)
#
#sentence = '6.0002 is the greatest'
#L = [word[0] for word in sentence.split(' ')]
#print(L)
#
#D = {word[0]:sentence.count(word[0])\
#     for word in sentence.split(' ')}
#print(D)
#
#
#def getSomething(n):
#    return [p for p in range(2, n+1)\
#            if 0 not in [p%d for d in range(2, p)]]
#    
#D = {i+1:getSomething(100)[i]\
#     for i in range(len(getSomething(100)))}
#print(D)
