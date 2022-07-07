# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -sys.maxsize
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.ans
    
        
    def traverse(self, root):
        if not root: return 0
        
        left_max = self.traverse(root.left)
        right_max = self.traverse(root.right)
        
        curr_max = left_max + root.val + right_max
        self.ans = max(self.ans, curr_max)
        
        return max(left_max+root.val, right_max+root.val, 0)
            