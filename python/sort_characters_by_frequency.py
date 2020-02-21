# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:58:44 2020

@author: shrey
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        #counter solution 
        from collections import Counter
        return ''.join([val*key for key, val in Counter(s).most_common()])