# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:33:17 2020

@author: shrey
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}
        
        for i, num in enumerate(nums):
            comp_num = target - num
            if comp_num in mapping:
                return [i, mapping[comp_num]]
            else:
                mapping[num] = i
                