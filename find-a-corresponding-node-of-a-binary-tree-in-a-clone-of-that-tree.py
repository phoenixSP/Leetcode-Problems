# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:04:02 2020

@author: shrey
"""

def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #dfs inorder traversal    
    if original is None or cloned is None or target.val == original.val:
        return cloned
    
    res1 = self.getTargetCopy(original.right, cloned.right, target)
    
    if res1 is not None:
        return res1
    
    return self.getTargetCopy(original.left, cloned.left, target)

    
    #bfs traversal 
    queue = []
    if original == None:
        return None
    queue.append([original, cloned])
    while queue:
        ori,cl = queue.pop(0)
        if ori.val == target.val:
            return cl
        if ori.left:
            queue.append([ori.left, cl.left])
        if ori.right:
            queue.append([ori.right, cl.right])