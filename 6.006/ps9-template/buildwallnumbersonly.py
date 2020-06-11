#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:55:24 2019

@author: lydiayu
"""

def build_wall(B):
    '''
    Input:  B | a border plan corresponding to 
              | a length-5 array of length-n strings 
    Output: P | a complete non-overlapping placement for B
              | that minimizes the number of cube stones used
     c1 = []
    for i in range(len(B)):
        c1.append(B[0][i])
    c2 = []
    for i in range(len(B)):
        c2.append(B[1][i])
    '''
    P = []
    
    columns = [] #convert B into a list of lists, where the lists are each column in B
    for i in range(len(B[0])):
        col = []
        for j in range(len(B)):
            col.append(B[j][i])
        columns.append(col)
    memos = dict()
    numBlocks = x(columns, 0, memos)

    print(numBlocks)
    return P

   
def x(c, i, memos):
    memoKey = "".join(letter for row in c for letter in row)
    if memoKey in memos:
        return memos[memoKey]
    
    lastCol = len(c)-1
    if i == lastCol and f(c[i]) == -1: #base case
        return 0
    
    if f(c[i]) == -1: #if c1 is full, go to next column
        return x(c, i+1, memos)
        
      
    blockPlacement1 = f(c[i])
    c[i] =  placeBlock(c[i], f(c[i])) 
    blocks1 = x(c, i, memos) + 1 #min num blocks if you place 1x1
    c[i][blockPlacement1] = "."
    

    blocksR = float("inf")
    if i < len(c)-1 and c[i+1][f(c[i])] == ".": #check that c1 and c2 have the same index free
        blockPlacementR = f(c[i])
        placeBlock(c[i], blockPlacementR)
        placeBlock(c[i+1], blockPlacementR)
        blocksR = x(c, i, memos) #min num blocks if you place 2x1 right
        c[i][blockPlacementR] = "."
        c[i+1][blockPlacementR] = "."
    
    blocksD = float("inf")
    if f(c[i]) < len(c[i]) -1 and c[i][f(c[i]) + 1] == ".": #make sure that there are 2 adjacent spaces free in c1
        blockPlacementD = f(c[i])
        placeBlock(placeBlock(c[i], blockPlacementD), blockPlacementD+1)
        blocksD = x(c, i, memos) #min num blocks if you place 2x1 down
        c[i][blockPlacementD] = "."
        c[i][blockPlacementD+1] = "."
    
    numBlocks = min(blocks1, blocksR, blocksD)
    memos[memoKey] = numBlocks
    
    return numBlocks

def f(column): #return index of first empty cell in column c
    for i in range(len(column)):
        if column[i] == ".":
            return i
    return -1

def placeBlock(column,j): #change c so that cell at index j is "b"
    column[j] = "b"
    return column