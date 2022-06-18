# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if not root: return 
            
            traverse(root.left)
            
            self.ans += 1
            
            traverse(root.right)
        traverse(root)
        return self.ans 