# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def find_level(root):
            if not root: return 0
            nonlocal diameter
            
            left = find_level(root.left)
            right = find_level(root.right)
            
            # print(root.val, left, right)
            
            diameter = max(diameter, left+right)
            return max(left, right) + 1
        find_level(root)
        return diameter