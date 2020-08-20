# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:08:56 2020

@author: shrey
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        
        neg = False
        
        if x < 0:
            neg = True
            
        
        
        reverse = 0
        
        x = -x if neg == True else x
        
        while x>0:
            
            reverse = reverse*10 + x%10
            x = x//10
            
        if (neg and reverse > pow(2,31)) or (reverse > pow(2,31) - 1):
            return 0
        
        return reverse*(-1 if neg else 1)