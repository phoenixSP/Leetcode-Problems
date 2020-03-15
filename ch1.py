# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:41:00 2020

@author: shrey
"""

def luckyNumbers(matrix):
    ans = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = matrix[i][:]
            print(row)
            column = [x[j] for x in matrix]
            print(column)
            if sorted(row)[0] == sorted(column)[-1]:
                ans.append(sorted(row)[0])             
    return ans


matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(luckyNumbers(matrix))
