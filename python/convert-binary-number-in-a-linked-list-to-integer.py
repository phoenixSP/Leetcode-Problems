# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:49:25 2020

@author: shrey
"""
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        number = 0
        
        while head is not None:
            number = number*2 + head.val
            head = head.next
            
        return number
        
