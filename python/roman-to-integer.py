# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:15:40 2020

@author: shrey
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        for i in range(len(s)):
            number += mapping[s[i]]
            
            if i > 0 and mapping[s[i]] > mapping[s[i-1]]:
                number -= 2*mapping[s[i-1]]
        
        return number
            