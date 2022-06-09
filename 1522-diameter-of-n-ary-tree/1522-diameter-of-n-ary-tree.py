"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        diameter = 0
        def get_level(root):
            if len(root.children) == 0:
                return 1
            nonlocal diameter
            max_first, max_sec = 0, 0 
            for child in root.children:
                parent_h = get_level(child)
                if parent_h > max_first:
                    max_first, max_sec = parent_h, max_first
                elif parent_h > max_sec:
                    max_sec = parent_h
            
            diameter = max(diameter, max_first + max_sec)
            
            return max_first + 1
        get_level(root)
        return diameter