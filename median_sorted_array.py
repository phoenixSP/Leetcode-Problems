# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:22:28 2019

@author: shrey
"""
import sys
def median_sorted_array(arrayX,arrayY):
    MAXSIZE=sys.maxsize    
    Y, X=arrayX, arrayY
    if len(X)>len(Y):
        X, Y =arrayX, arrayY
    
    start=0
    end=len(X)
            
    while start<=end:
        partitionX=int((start+end)/2)
        partitionY=int((len(X)+len(Y)+1)/2)-partitionX
        
        if partitionX==0:
            maxX=-MAXSIZE
            minX=X[partitionX]
        elif partitionX==len(X):
            minX=MAXSIZE
            maxX=X[partitionX-1]
        else:
            maxX=X[partitionX-1]
            minX=X[partitionX]
            
        if partitionY==0:
            maxY=-MAXSIZE
            minY=Y[partitionY]
        elif partitionY==len(Y):
            minY=MAXSIZE
            maxY=Y[partitionY-1]
        else:
            maxY=Y[partitionY-1]
            minY=Y[partitionY]
     
        if maxX<minY and maxY<minX:
            if (len(X)+len(Y))%2==0:
                return  0.5*(max(maxX,maxY)+min(minX,minY))
            else:
                return max(maxX,maxY)
        elif maxX>minY:
            end=partitionX
        elif maxY>minX:
            start=partitionX+1
    
        
    
X=[3,4]
Y=[1,2]
median=median_sorted_array(X,Y)
print(median)
    
    
        
        
        
        