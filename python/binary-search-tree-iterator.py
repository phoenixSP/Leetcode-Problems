# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:47:32 2020

@author: shrey
"""

#O(n) memory complexity
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.inorderList = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.inorderList.append(node.val)
            inorder(node.right)
            
        inorder(root)        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.inorderList.pop(0)
            
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.inorderList

        
#O(h) memory complexity
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.q = []
        self.root = root
        node = root
        while node:
            self.q.append(node)
            node = node.left
            

    def next(self) -> int:
        """
        @return the next smallest number
        """
        curr = self.q.pop()
        nextNode = curr.right
        
        while nextNode:
            self.q.append(nextNode)
            nextNode = nextNode.left
            
        return curr.val
        
            
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        
        return self.q        