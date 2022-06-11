# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = []
        
        def dfs(root, curr_max):
            if not root: return
            
            curr_max = max(curr_max, root.val)
            
            if curr_max == root.val:
                res.append(root.val)
            
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
            
        dfs(root, -sys.maxsize)
        return len(res)
        