# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def find_level(root, level):
            if not root: return level
            
            left = find_level(root.left, level+1)
            right = find_level(root.right, level+1)
            
            if abs(left - right) > 1:
                self.ans = False
            
            return max(left, right)
    
        find_level(root,0)
        return self.ans