# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:53:57 2020

@author: shrey
"""

from collections import defaultdict
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        #the method is to replace the characters in t that are absent in s with  characters that are present in s
        #the number of times we need to do this is #extra characters in t (since s and t are equal sized)
        
        character_dict = {}
        count = 0
        #assumption: length same, and letters are all lowe-case
        
        for ch in s:
            character_dict.setdefault(ch, 0)
            character_dict[ch]+= 1
            
        for ch in t:
            character_dict.setdefault(ch, 0)
            character_dict[ch]-= 1
            if character_dict[ch] < 0:
                count += 1 #assuming replacement of a particular character is considered one action; if each letter had to be replaced individually,
                #the count would be count+= abs(character_dict[ch])
                
        return count
    
        #Default dict method
        
        character_dict = defaultdict(lambda: 0) #decrease of runtime 
        count = 0
        #assumption: length same, and letters are all lowe-case
        
        for ch in s:
            character_dict[ch]+= 1
            
        for ch in t:
            character_dict[ch]-= 1
            if character_dict[ch] < 0:
                count += 1 #assuming replacement of a particular character is considered one action; if each letter had to be replaced individually,
                #the count would be count+= abs(character_dict[ch])
                
        return count
    
        #using vanilla dictionary with checks for presence of character had similar results as default dict

        #counter implementation
        #idea is look at characters that are at surplus in s, thus they need to be added in s by replacement
        
        temp = Counter(s) - Counter(t)
        return sum(max(0, temp[ch]) for ch in set(s))
    
    