# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None
        self.k = None
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inorderTraverse(root)
        return self.ans 
        
    def inorderTraverse(self, root):
        if not root: return 
        
        self.inorderTraverse(root.left)
        
        self.k -= 1
        if self.k == 0:
            self.ans = root.val 
        
        self.inorderTraverse(root.right)