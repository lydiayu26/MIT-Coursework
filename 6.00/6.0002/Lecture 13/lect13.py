#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers
plt.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
plt.rcParams['legend.numpoints'] = 1

random.seed(1)
   
def findProb(numCommunities, community,
              casesPerTrial, multiple, numTrials):
    numTimesOver = 0
    threshhold = (casesPerTrial/numCommunities)*multiple
    for t in range(numTrials):
        cases = [0]*numCommunities
        for i in range(casesPerTrial):
            cases[random.choice(range(numCommunities))] += 1
        if cases[community] > threshhold:
            numTimesOver += 1
    prob = round(numTimesOver/numTrials, 4)
    print('Est. prob. of it being a random event =', prob)
    
#Initialize constants
numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize//communitySize
multiple = 1.3

casesPerTrial = numCasesPerYear*numYears
findProb(numCommunities, 111, casesPerTrial, multiple, 100)
