# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        self.found = False
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        if len(nodes) == 1: return nodes[0]
        def find(root):
            if not root:
                return []
            left = find(root.left)
            right = find(root.right)
            
            mix = left + right
            if root in nodes:
                mix.append(root.val)
            
            if len(mix) == len(nodes) and not self.found:
                self.ans = root
                self.found = True
            return mix
        find(root)
        return self.ans
            