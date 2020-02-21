# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:40:12 2019

@author: shrey
"""

def findShortestLength(strs):
    min_len = 1000000
    for i, s in enumerate(strs):
        if len(s) < min_len:
            min_len = len(s)
    return min_len 
    

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    
    start = 0
    end = findShortestLength(strs) - 1 
    print(end)
    
    while start <= end:
        mid = int((start + end)/2)
        if inAllStrings(strs, mid):
            start = mid + 1
        else:
            end = mid - 1
        
    return strs[0][:int((start+end)/2) + 1]

def inAllStrings(strs, pos): 
    idx = pos + 1
    substring = strs[0][:idx]
    for s in strs[1:]:
        if not s.startswith(substring):
            return False
    return True
           
strs = ["flower","flow","flight"] 
prefix = longestCommonPrefix(strs)