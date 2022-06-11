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
            if not root: return level, True
            
            left, ans1 = find_level(root.left, level+1)
            right, ans2 = find_level(root.right, level+1)
            
            ans = True
            if abs(left - right) > 1:
                ans = False
            if ans1 and ans2:
                return max(left, right), ans
            else:
                return max(left, right), False

        h, ans = find_level(root,0)
        return ans 