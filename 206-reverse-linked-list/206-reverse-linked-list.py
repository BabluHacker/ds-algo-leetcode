# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currNode = head
        
        while(currNode):
            nextNode = currNode.next

            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode
            
        
        
        
        # return self.recurseRevList(head)
    
#     def recurseRevList(self, head ):
#         if head == None or head.next == None: return head
        
#         p = self.recurseRevList(head.next)
#         head.next.next = head
#         head.next = None
        
#         return p
        
    