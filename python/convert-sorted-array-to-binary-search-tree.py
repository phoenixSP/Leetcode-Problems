# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:46:58 2020

@author: shrey
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None
        
        mid = int(len(nums)/2)
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root