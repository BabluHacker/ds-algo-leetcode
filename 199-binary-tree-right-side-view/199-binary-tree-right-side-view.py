# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traverse and put the last node of every level 
        if not root : return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                child = queue.pop(0)
                tmp.append(child.val)
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
                
            res.append(tmp[-1])
        return res
                