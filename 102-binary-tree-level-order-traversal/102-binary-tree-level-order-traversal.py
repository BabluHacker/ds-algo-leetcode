# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # iterative BFS
        
        if not root: return []
        queue = []
        queue.append(root)
        result = []
        
        while queue:
            
            tmp = []
            for i in range(len(queue)):
                child = queue.pop(0)
                tmp.append(child.val)
                
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
            result.append(tmp)
        
        return result

        # recursive
    
#         levels = []
#         if not root: return levels
        
        
#         def levelTraverse(root, level):
#             if len(levels) == level:
#                 levels.append([])
                
#             levels[level].append(root.val)
            
#             if root.left:
#                 levelTraverse(root.left, level+1)
#             if root.right:
#                 levelTraverse(root.right, level+1)
#         levelTraverse(root, 0)     
#         return levels
                
        