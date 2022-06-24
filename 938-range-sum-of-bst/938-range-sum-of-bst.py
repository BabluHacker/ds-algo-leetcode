# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def get_sum(root):
            if not root: return
            get_sum(root.left)
            if low <= root.val <= high:
                self.ans += root.val
            get_sum(root.right)
        
        get_sum(root)
        return self.ans 