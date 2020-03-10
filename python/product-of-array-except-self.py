# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:08:00 2020

@author: shrey
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp_left = [1]*len(nums)
        temp_right = [1]*len(nums)
        res = [0]*len(nums)
        for i in range(1, n):
            temp_left[i] = nums[i-1]*temp_left[i-1]
            
        for i in range(n-2, -1, -1):
            temp_right[i] = nums[i+1]*temp_right[i+1]
            
        for i in range(n):
            res[i] = temp_left[i]*temp_right[i]
            
        return res