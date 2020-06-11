# -*- coding: utf-8 -*-

import math, numpy as np
import matplotlib.pyplot as plt
import random


random.seed(1)

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2
    
#xVals, yVals = [], []
#mu, sigma = 0, 1
#x = -6
#step = 0.05
#while x < 6:
#    xVals.append(x)
#    yVals.append(gaussian(x, mu, sigma))
#    x += step
#plt.plot(xVals, yVals)
#plt.title('Normal Distribution, mu = ' + str(mu)\
#            + ', sigma = ' + str(sigma))
#
#mu = 0
#numSamples = 1000000
#for sigma in (1, 10):
#    plt.figure()
#    dist = []
#    for i in range(numSamples):
#        dist.append(random.gauss(mu, sigma))
#    plt.hist(dist, bins = 100)
#    plt.xlabel('Value')
#    plt.ylabel('Frequency')
#    plt.title('Normal Distribution, mu = ' + str(mu)\
#                + ', sigma = ' + str(sigma))

import scipy.integrate

def checkEmpiricalNorm(numTrials):
    for t in range(numTrials):
        mu = random.randint(-100, 100)
        sigma = random.randint(1, 100)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian,
                                        mu-numStd*sigma,
                                        mu+numStd*sigma,
                                        (mu, sigma))[0]
            print(' Fraction within', numStd, 
                  'std =', round(area, 4))
            
#checkEmpiricalNorm(5)

def choose(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def binomial(n,k,p):
    return choose(n,k)*(p**k)*((1-p)**(n-k))
    
def plotBinomial(n, p, title, xLabel, yLabel):
    xVals = []
    yVals = []
    for i in range(n+1):
        xVals.append(i)
        yVals.append(binomial(n,i,p))
    plt.figure() 
    plt.title(title) 
    plt.xlabel(xLabel) 
    plt.ylabel(yLabel) 
    plt.plot(xVals, yVals) 

#plotBinomial(10, 0.5, 'Binomial Distribution, p = 1/2',
#             'Hits', 'Frequency')
#plotBinomial(100, 0.5, 'Binomial Distribution, p = 1/2',
#             'Hits', 'Frequency')

def checkEmpiricalBinomial(n, prob):
    mu = n*prob
    sigma = (n * prob * (1-prob))**0.5
    for numStd in (1.0, 1.96, 3.0):
        tot = 0
        for i in range(int(round(mu-numStd*sigma)),
                       int(round(mu+numStd*sigma)) + 1):
            tot += binomial(n, i, prob)
        print(' Fraction within', numStd, 'std =',
              round(tot, 4)) 
        
#for n in (50, 1000):
#    for prob in (0.5, 0.75):
#        print('For n =', n, 'prob =', prob)
#        checkEmpiricalBinomial(n, 0.5)

def checkEmpiricalUniform(n, a, b):
    mu = (b-a)/2
    sigma = (b-a)/(12**0.5)
    print('mu =', mu, '  sigma =', sigma)
    for numStd in (1, 1.96, 3):
        tot = 0
        for i in range(n):
            val = random.uniform(a, b)
            tot += (1 if abs(mu-val) <= numStd*sigma\
                    else 0)
        print('  Fraction within', numStd, 'std =',
              tot/n)
    
#checkEmpiricalUniform(100000, 0, 100)

def checkEmpiricalExponential(n, lambd):
    mu = 1/lambd
    sigma = mu
    print('mu =', mu, '  sigma =', sigma)
    for numStd in (1, 1.96, 3):
        tot = 0
        for i in range(n):
            val = random.expovariate(lambd)
            tot += (1 if abs(mu-val) <= numStd*sigma\
                    else 0)
        print('  Fraction within', numStd, 'std =',
              tot/n)
        
checkEmpiricalExponential(100000, 1/10)

random.seed(0)       
def genGradesU(numGrades, noise):
    grades = []
    for i in range(numGrades):
        grades.append(min(100,
                      int(random.choice(range(0, 101))\
                      + abs(random.gauss(5, noise)))))
    return grades 
     
def genGradesG(numGrades):
    grades = []
    for i in range(numGrades):
        grades.append(int(random.gauss(52, 8)))
    return grades 
     
def genGradesE(numGrades):
    grades = []
    for i in range(numGrades):
        grade = random.expovariate(1/30)
        if grade >= 0 and grade <= 100:
            grades.append(100 - round(grade))
    maxG = max(grades)
    grades = (np.array(grades)/maxG)*100
    return grades
   
#grades = genGradesU(400, 0)
#grades = genGradesG(400)
#grades = genGradesE(500)
#plt.hist(grades)
#mean = round(sum(grades)/len(grades))
#std = round(np.std(grades))
#plt.xlabel('Grade')
#plt.ylabel('Frequency')
#plt.title('Distribution of Grades\n' +\
#          '(mean = ' + str(mean) +\
#          ', std = ' + str(std) + ')')
#print('mean =', mean, 'std =', std)
#tot = 0
#for g in grades:
#    if g + 1.5*std < mean:
#        tot += 1
#print('Fraction more than 1.5 std below mean =',
#      tot/len(grades))



