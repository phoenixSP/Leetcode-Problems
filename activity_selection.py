# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 06:33:29 2019

@author: shrey
"""

#https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

def activity_selection(start,end):
    start, end=[x for _,x in sorted(zip(end,start))], sorted(end)
    print(start)
    print(end)
    i=0
    print(0)
    for j in range(1,len(start)):
        if end[i]<=start[j]:
            print("[",start[j],",",end[j],"],")
            print(j)
            i=j
    
start = [1 , 3 , 0 , 5 , 8 , 5] 
end =   [2 , 4 , 6 , 7 , 9 , 9]

activity_selection(start,end)