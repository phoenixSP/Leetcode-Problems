# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:27:25 2020

@author: shrey
"""
#does not handle top to bottom order
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        

        def dfs(root, number):
            
            if not root:
                return []
            
            res = []
            res.append([root.val, number])
            res = res + dfs(root.left, number - 1)
            res = res + dfs(root.right, number + 1)
            
            return res
        
        res = dfs(root, 0)
        tree_dict = {}
        
        for element in res:
            val, idx = element
            
            if idx in tree_dict:
                tree_dict[idx].append(val)
            else:
                tree_dict[idx] = [val]

        final = []
        
        for i in sorted(tree_dict):
            final.append(sorted(tree_dict[i]))
        return final          