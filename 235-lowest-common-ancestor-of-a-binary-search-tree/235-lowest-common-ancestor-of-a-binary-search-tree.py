# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def searchLCA(root, p, q):
            
            if root.val == p.val or root.val == q.val:
                return root
            
            # check if all p,q are on left
            if p.val < root.val and q.val < root.val:
                return searchLCA(root.left, p, q)
            # check if all p,q are on right
            elif p.val > root.val and q.val > root.val:
                return searchLCA(root.right, p, q)
            else: # splitting p, q then root is the ans
                return root
        return searchLCA(root,p,q)