# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:48:26 2020

@author: shrey
"""

from collections import defaultdict 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0
        prevSum = defaultdict(lambda: 0)
        
        for num in nums:
            currSum += num
            
            if currSum == k:
                res += 1 
                
            if currSum - k  in prevSum:
                res += prevSum[currSum - k]
                
            prevSum[currSum] += 1
            
        return res