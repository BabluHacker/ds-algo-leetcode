# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(root)
        
        while queue:
            r = queue.pop()
            if self.checkIsSame(r, subRoot):
                return True
            if r.left: 
                queue.append(r.left)
            if r.right: 
                queue.append(r.right)
            
        return False
        

        
    def checkIsSame(self, curr, sub):
        if not curr and not sub:
            return True
        if not curr or not sub:
            return False
        if curr.val != sub.val:
            return False
        return self.checkIsSame(curr.left, sub.left) and self.checkIsSame(curr.right, sub.right)
        