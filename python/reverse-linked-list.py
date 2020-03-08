# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:04:55 2020

@author: shrey
"""

######################## ITERATIVE SOLUTION ##############################################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr = head
        next = None
        prev = None
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
            
        return prev


####################################### RECURSIVE SOLUTION #########################################
class Solution:
    def reverseListUtil(self, curr, prev):
        
        if curr:
            next = curr.next
            curr.next = prev
            return self.reverseListUtil(next, curr)
        
        else:
            return prev
        
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseListUtil(head, None)
        