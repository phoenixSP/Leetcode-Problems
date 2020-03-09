# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:07:46 2020

@author: shrey
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = { ')':'(', '}':'{', ']':'['}
        
        if len(s) == 0:
            return True
        
        for i in s:
            if i in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[i]:
                    return False
            else:
                stack.append(i)
        
        if len(stack)> 0:
            return False
        else:
            return True