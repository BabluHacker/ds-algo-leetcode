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
            all_levels = []
            # print(root.val)
            for child in root.children:
                l = get_level(child)
                all_levels.append(l)
            # print(all_levels)
            max_first = max(all_levels)
            del all_levels[all_levels.index(max_first)]
            if len(all_levels)>0: max_sec = max(all_levels)
            else: max_sec = 0
            diameter = max(diameter, max_first + max_sec)
            
            return max_first + 1
        get_level(root)
        return diameter