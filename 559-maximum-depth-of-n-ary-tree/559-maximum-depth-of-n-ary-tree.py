"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = [root]
        depth = 0
        
        while q:
            l = len(q)
            depth += 1
            for i in range(l):
                node = q.pop(0)
                for child in node.children:
                    q.append(child)
        
        
        return depth