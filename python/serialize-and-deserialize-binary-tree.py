# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:38:22 2020

@author: shrey
"""

#level order method (BFS)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return None
        
        serialize = []
        
        q = [root]
        
        while q:
            node = q.pop(0)
            if node: 
                q.append(node.left)
                q.append(node.right)
                serialize.append(str(node.val))
            else:
                serialize.append("None")

        return ",".join(serialize).strip("#")
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        nodes = data.split(",")
                
        #nodes = [None if x == 'None' else int(x) for x in nodes]
        
        serialized_nodes = list(map(lambda x : None if x == "None" else int(x), nodes))
        
        root = TreeNode(serialized_nodes.pop(0))
        q = [root]
        
        while serialized_nodes and q:
            node = q.pop(0)
            left_val = serialized_nodes.pop(0)
            right_val = serialized_nodes.pop(0)
            
            if left_val is not None:
                node.left = TreeNode(left_val)
                q.append(node.left)
                
            if right_val is not None:
                node.right = TreeNode(right_val)
                q.append(node.right)
                
        return root
    
#        #serialized_nodes = list(map(lambda x : None if x == "None" else int(x), nodes))
#        
#        serialized_nodes = nodes
#        
#        root = TreeNode(int(serialized_nodes.pop(0)))
#        q = [root]
#        
#        while serialized_nodes and q:
#            node = q.pop(0)
#            left_val = serialized_nodes.pop(0)
#            right_val = serialized_nodes.pop(0)
#            
#            if left_val != "None":
#                node.left = TreeNode(int(left_val))
#                q.append(node.left)
#                
#            if right_val != "None":
#                node.right = TreeNode(int(right_val))
#                q.append(node.right)
    
    
    
#Preorder method  
class Codec:

    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeUtil(root):
            
            if not root:
                return ["None"]
            
            res = []
            
            if root:
                res.append(str(root.val))
                res = res + serializeUtil(root.left)
                res = res + serializeUtil(root.right)
            else:
                res.append("None")
                
            return res
        
        serialize =  serializeUtil(root)
        return ",".join(serialize)
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        data = data.split(',')
        
        def deserializeUtil():
            val = data.pop(0)
            if val == "None":
                root = None
            else:
                root = TreeNode(int(val))
                root.left = deserializeUtil()
                root.right = deserializeUtil()

            return root
        
        return deserializeUtil()
        
        serialize =  serializeUtil(root)
        return ",".join(serialize)