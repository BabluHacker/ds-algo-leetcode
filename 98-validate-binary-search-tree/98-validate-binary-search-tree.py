# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.validate(root, -sys.maxsize-1, sys.maxsize)
    def validate(self, root, min_val, max_val):
        if not root: return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)
    