# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:54:31 2019

@author: shrey
"""
import collections
#problem number 314

class Node():
    def __init__(self,val):
        self.val=val
        self.left=self.right=None
        
class Tree(Node):
    def get_min_max(self,root,minimum, maximum,hd):
        if root is None:
            return
        
        if minimum[0]>hd:
            minimum[0]=hd
        elif maximum[0]<hd:
            maximum[0]=hd
            
        self.get_min_max(root.left,minimum, maximum, hd-1)
        self.get_min_max(root.right,minimum, maximum, hd+1)   
        
        
    def print_vertical_line(self,root,line_no,hd):
        if root is None:
            return
        
        if line_no==hd:
            print(root.val)
        
        self.print_vertical_line(root.left,line_no, hd-1)
        self.print_vertical_line(root.right,line_no, hd+1)
        
    '''
    The maximum and minimum width is calsulated by traversing through the tree
    Time:O(w*n) where w is width
         0(n^2) in worst case
         
    '''    
    def print_vertical_order1(self,root):
        minimum=[0]
        maximum=[0]
        self.get_min_max(root,minimum,maximum,0)
        
        for i in range(minimum[0],maximum[0]+1):
            self.print_vertical_line(root,i,0)
            print
            
    def print_vertical_order2(self,root):
        if root is None:
            return
        
        queue=[]
        hd_dict={}
        queue.append(root)
        hd_dict[0]=[root.val]
        
        hd={}
        hd[root]=0
        
        while len(queue)>0:
            enq=queue.pop(0)
            if enq.left is not None:
                queue.append(enq.left)
                hd[enq.left]=hd[enq]-1
                if hd_dict.get(hd[enq.left]) is None:
                    hd_dict[hd[enq.left]]=[]
                hd_dict[hd[enq.left]].append(enq.left.val)
                
            if enq.right is not None:
                queue.append(enq.right)
                hd[enq.right]=hd[enq]+1
                if hd_dict.get(hd[enq.right]) is None:
                    hd_dict[hd[enq.right]]=[]
                hd_dict[hd[enq.right]].append(enq.right.val)
                
        hd_dict_sorted=collections.OrderedDict(sorted(hd_dict.items()))     
        
        for i in hd_dict_sorted.values(): 
            for j in i: 
                print(j, " ", end="") 
            print()     


        
    def inorder(self,root):
        if root is not None:
           self.inorder(root.left)
           print(root.val)
           self.inorder(root.right)
           
tree=Tree(3)
tree.left=Node(4)
tree.right=Node(9)
tree.right.right=Node(8)
#tree.inorder(tree)
tree.print_vertical_order2(tree)