# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:55:52 2020

@author: shrey
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        #replace by count when count > 1
        
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                print('In else')
                if count>1:
                    for k, item in enumerate(str(count)):
                        chars.insert(i+1+k, item)
                    count = 1