# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:17:43 2020

@author: shrey
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #use Floyd's cycle finding algo
        
        slow = fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
            if slow == fast:
                return True
                """ 
                #code for getting the location of the loop 
                
                m = 1
                slow = head 
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    m += 1
                    
                    if slow == fast:
                        return m
                    """
        return False
            