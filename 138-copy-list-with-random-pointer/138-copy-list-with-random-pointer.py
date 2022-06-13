"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        oldToCopy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next 
        
        
        new_head = curr = oldToCopy[head]
        
        while head:
            curr.next = oldToCopy[head.next] if head.next else None
            curr.random = oldToCopy[head.random] if head.random else None
            
            head = head.next 
            curr = curr.next 
        return new_head 