# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:07:23 2019

@author: shrey
"""

#find kth largest element in a datastream. Leetcode 703

import heapq

class kth_largest_in_datastream():
    def __init__(self, array,k):
        self.minHeap=array
        heapq.heapify(self.minHeap) #returns NULL
        self.k=k
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        
    def add_number(self,number):
        if len(self.minHeap)<self.k:
            heapq.heappush(self.minHeap,number)
        else:
            if self.minHeap[0]<number:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap,number)
                
    def get_kth_largest(self):
        return self.minHeap[0]
    
array=[1,2,3,4,5]
sol=kth_largest_in_datastream(array,3)
print(sol.get_kth_largest())
sol.add_number(8)
print(sol.get_kth_largest())
sol.add_number(10)
print(sol.get_kth_largest())
sol.add_number(17)
print(sol.get_kth_largest())
                