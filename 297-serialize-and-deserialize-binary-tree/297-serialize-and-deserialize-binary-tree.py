# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def encode(root):
            if not root:
                ans.append(None)
                return
            ans.append(root.val)
            encode(root.left)
            encode(root.right)
        
        encode(root)
        # print(ans)
        return "#".join(map(str, ans))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split("#")
        
        def decode(idx):
            if data[idx] == 'None':
                return None, idx
            
            root = TreeNode(int(data[idx]))
            root.left, idx = decode(idx+1)
            root.right, idx = decode(idx+1)
            return root, idx
        root, idx = decode(0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))