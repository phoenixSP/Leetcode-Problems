# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:05:21 2020

@author: shrey
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        k = ceil(sqrt(2*n))
        
        for i in range(k,0,-1):
            if i*(i+1) <= 2*n:
                return i 