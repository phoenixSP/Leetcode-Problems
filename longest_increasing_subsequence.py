# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:53:50 2019

@author: shrey
"""

def longest_increasing_subsequence(array):
    T=[1]*len(array)
    
    for i in range(1,len(array)):
        for j in range(i):
            if array[j]<array[i]:
                T[i]+=1
    return T[-1]
            
array=[3,4,-1,0,6,2,3]
print(longest_increasing_subsequence(array))