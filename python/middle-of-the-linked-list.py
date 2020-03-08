# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:51:28 2020

@author: shrey
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        curr_step2 = curr_step1 = head
        
        while curr_step2 and curr_step2.next:
            curr_step1 = curr_step1.next
            curr_step2 = curr_step2.next.next
            
        return curr_step1