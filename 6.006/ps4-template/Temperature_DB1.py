#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 01:24:22 2019

@author: lydiayu
"""

from Binary_Tree_Set import BST_Node, Binary_Tree_Set
# ----------------------------------- #
# DO NOT REMOVE THIS IMPORT STATEMENT # 
# DO NOT MODIFY IMPORTED CODE         #
# ----------------------------------- #

class Temperature_DB_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        if A.left is None:
            A.min_date = A.item.key
        if A.right is None:
            A.max_date = A.item.key
        elif A.left:
            A.min_date = A.left.min_date
        if A.right:
            A.max_date = A.right.max_date
        if A.left is None and A.right is None:
            A.max_temp = A.item.temp
        elif A.left is None and A.right:
            A.max_temp = max(A.item.temp, A.right.max_temp)
        elif A.right is None and A.left:
            A.max_temp = max(A.item.temp, A.left.max_temp)
        elif A.right and A.left:
            A.max_temp = max(A.item.temp, A.right.max_temp, A.left.max_temp)

    def subtree_max_in_range(A, d1, d2):
        max_temp = None
        if d1<=A.min_date<=A.max_date<=d2:
            return A.max_temp
        elif d1 > A.max_date or d2 < A.min_date:
            return None
        else:
            if d1<=A.item.key<=d2:
                max_temp = A.item.temp
            if A.left:
                lm = A.left.subtree_max_in_range(d1,d2)
                if lm:
                    if (not max_temp or lm>max_temp):
                        max_temp=lm
            if A.right:
                rm = A.right.subtree_max_in_range(d1,d2)
                if rm:
                    if (not max_temp or rm>max_temp):
                        max_temp = rm
        return max_temp