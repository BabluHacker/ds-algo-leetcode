# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def preorder(root):
            if not root: return None
            if not root.left and not root.right:
                return root
            
            leftTail = preorder(root.left)
            rightTail = preorder(root.right)
            
            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
                
            return rightTail if rightTail else leftTail
        preorder(root)
        