# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:44:23 2020

@author: shrey
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = curr = ListNode(0)
                
        while l1 and l2:
            
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
                
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
            
        return root.next