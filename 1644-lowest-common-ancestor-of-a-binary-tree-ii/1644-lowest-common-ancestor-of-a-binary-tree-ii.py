# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
            self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def find(root):
            if not root: return False
            
            left = find(root.left)
            right = find(root.right)
            
            if p.val == root.val or q.val == root.val:
                mid = True
            else:
                mid = False
            
            if (mid and left) or (mid and right) or (left and right):
                self.ans = root
                
            return (mid or left or right)
        find(root)
        return self.ans 