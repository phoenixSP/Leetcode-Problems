# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:51:48 2019

@author: shrey
"""

#find median in a data stream: leetcode 295
import heapq

class Solution:
    def __init__(self):
        self.lower=[]
        self.higher=[]
        
    def addNumber(self,number):
        if len(self.lower)==0 or number<-self.lower[0]:
            heapq.heappush(self.lower,-number)
        else:
            heapq.heappush(self.higher,number)
            
        if len(self.lower)-len(self.higher)>=2:
            element=heapq.heappop(self.lower)
            heapq.heappush(self.higher,-element)
        
    def findMedian(self):
        if len(self.lower)==len(self.higher):
            return (-self.lower[0]+self.higher[0])/2
        else:
            return -self.lower[0]
        
sol=Solution()
sol.addNumber(5)
print(sol.findMedian())
sol.addNumber(4)
print(sol.findMedian())
sol.addNumber(3)
print(sol.findMedian())
sol.addNumber(3)
print(sol.findMedian())
sol.addNumber(3)
print(sol.findMedian())