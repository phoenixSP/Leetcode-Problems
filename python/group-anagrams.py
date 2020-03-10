# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:35:42 2020

@author: shrey
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if ''.join(sorted(s)) in mapping:
                mapping[sorted_str].append(s)
            else:
                mapping[sorted_str] = [s]
                
        return mapping.values()