# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:37:56 2019

@author: shrey
"""
#problem 28 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1 
        for i in range(0, len(haystack) - len(needle) + 1):
            #print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle: 
                return i
        return -1 
        #return haystack.find(needle)