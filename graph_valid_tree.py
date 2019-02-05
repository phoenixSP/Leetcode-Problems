# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:24:17 2019

@author: shrey
"""
from collections import defaultdict

#Leetcode 261

class Solution:
    def __init__(self,adj_list=None, vertices=0):
        if adj_list==None:
            adj_list=defaultdict(list)
        self.__adj_list=adj_list
        self.__no_of_vertices=vertices
    
    def add_edge(self,src,dst): #undirectedgraph
            self.__adj_list[src].append(dst)
            self.__adj_list[dst].append(src)
 
    