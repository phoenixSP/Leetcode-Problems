# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:53:42 2020

@author: shrey
"""

import heapq

class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        wordDict = {}
        
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
                
            else:
                wordDict[word] = 1
                
        minheap = []
        
        for key, val in wordDict.items():
            if len(minheap) < k:
                heappush(minheap, Element(key, val))
                
            elif minheap[0] < Element(key,val):
                heappushpop(minheap, Element(key, val))
        
        res = []
        for i in range(k):
            res.append(heappop(minheap).word)
            
        return res[::-1]