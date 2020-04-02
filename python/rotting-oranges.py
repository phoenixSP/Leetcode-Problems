# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:57:03 2020

@author: shrey
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        
        #use set() for fresh because the time complexity of removal from list is O(n), set O(1)
        fresh = set()
        rotten = []
                
        time = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append([r,c, time])
                elif grid[r][c] == 1:
                    fresh.add((r,c))
                    
                    
        

        while rotten:
            x, y, time = rotten.pop(0)

            for dx, dy in directions: 
                if -1<x+dx<row and -1<y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy] = 2
                    fresh.remove((x+dx, y+dy))
                    rotten.append([x+dx, y+dy, time + 1])
                    
                    
        return time if not fresh else -1