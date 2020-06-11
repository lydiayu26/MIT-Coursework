#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:23:52 2018

@author: lydiayu
"""

def get_mean_std(X):
        mean = sum(X)/len(X)
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        std = (tot/len(X))**0.5
        return (mean, std)
    
    
X = [0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 2, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]

meanStd = get_mean_std(X)
avg = meanStd[0]
std = meanStd[1]
confInt = 1.96 * (std/((len(X))**0.5))

print(confInt)