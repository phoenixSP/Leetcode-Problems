# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:35:55 2020

@author: shrey
"""

from collections import defaultdict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        char_list = defaultdict(lambda: 0)
        
        for char in T:
            char_list[char] += 1
            
        

        res = ""    
        for char in S:
            if char in char_list:
                res += char*char_list[char]
                del char_list[char]
                
                
        if len(char_list) >0:
            for char in char_list:
                
                res += char*char_list[char]
                
        return res