# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:22:10 2019

@author: shrey
"""

#Problem: Defanging an IP Address
#problem number: 1108
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        
        s = re.sub('[^0-9a-zA-Z]+','',s)
        start = 0
        end = len(s) -1 
        #print(s)
        
        while start < end:
            if not s[start].isalnum():
                start += 1

            if not s[end].isalnum():
                end -= 1

            if s[start].lower() == s[end].lower():
                #print(s[start], start, '   ', s[end], end)
                start +=1 
                end -=1
            else:
                print('in false', s[start], start, '   ', s[end], end)
                return False
        
        return True