# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #iterative solution
        
#         queue = []
        
#         queue.append((1, root)) # storing depth and node
#         depth = 0
#         curr_depth = 0
#         while queue:
#             curr_depth, s = queue.pop(0)
            
#             # depth = max(depth, curr_depth)
#             if s:
#                 queue.append((curr_depth+1, s.left))
#                 queue.append((curr_depth+1, s.right))
            
#         return curr_depth-1
            
    
    #recursive solution
        return self.findDepth(root, 0)
    
    def findDepth(self, root, depth):
        if not root: return depth
        
        d1 = self.findDepth(root.left, depth+1)
        d2 = self.findDepth(root.right, depth+1)
        
        return max(d1, d2)
        
        