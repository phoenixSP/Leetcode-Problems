# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:04:25 2020

@author: shrey
"""

class Solution: 
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        res = None
        prev = res
        
        while l1 or l2:
            add = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = add//10
            d = add%10
            temp = ListNode(d)
            
            if res is None:
                res = temp
            else:
                prev.next = temp
                
            prev = temp
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
                
        if carry:
            temp.next = ListNode(carry)
            
        return res