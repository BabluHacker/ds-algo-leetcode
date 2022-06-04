# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        (self.invertBinaryTree(root))
        return root
        
    def invertBinaryTree(self, root):
        if not root.left and not root.right: # if leaf node then return that node
            return 
        
        root.left, root.right = root.right, root.left
        
        if root.left:
            self.invertBinaryTree(root.left)
        if root.right:
            self.invertBinaryTree(root.right)
        return 
        
        
        