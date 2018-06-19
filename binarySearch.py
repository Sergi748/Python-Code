# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:21:24 2018

@author: Sergio Campos
"""

vector = [5, 3, 7, 6, 2, 1, 4]

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1], x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
    
def binarySearch(x, element):
    
    toFound = element
    min = 0
    max = len(x) - 1
    ind = (min + max)//2
    
    while x[ind] != toFound:
        ind = (min + max)//2
        if x[ind] == toFound:
            return ind
        elif x[ind] < toFound:
            min = ind+1
        else:
            max = ind-1  

vector = quicksort(vector)    
binarySearch(vector, 6)

