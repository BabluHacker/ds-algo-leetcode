# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        return self.checkIsSame(p, q)
    
    def checkIsSame(self, left, right):
        if not left and not right: return True
        
        if not (left and right): return False
        
        if left.val != right.val: return False
        
        return self.checkIsSame(left.left, right.left) and self.checkIsSame(left.right, right.right)
    
        