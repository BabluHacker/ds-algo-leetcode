"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def clone(root):
            
            if not root:
                return None
            copy = Node(root.val)
            
            for n in root.children:
                copy.children.append(clone(n))
            return copy
        return clone(root)