# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:37:28 2019

@author: shrey
"""

def time_taken(layout, string):
    time = 0
    prev = 0
    for char in string.lower(): 
        now = layout.find(char)

        time += abs(prev - now)
        prev = now
        
    print(time)
    
#%%
time_taken('abc','abc')
        