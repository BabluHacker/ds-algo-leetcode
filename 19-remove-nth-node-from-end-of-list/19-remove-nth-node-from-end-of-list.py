# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        revHead = self.reverse(head)
        
        head = self.revDel(revHead, n)
        return head
    
    def reverse(self, head):
        dummyNext = head
        prev = None
        curr = head
        
        while curr:
            dummyNext = dummyNext.next
            curr.next = prev
            prev = curr
            curr = dummyNext
        return prev
    
    def revDel(self, head, n):
        dummyNext = head
        prev = None
        curr = head
        counter = 1
        while curr:
            dummyNext = curr.next 
            if counter == n:
                curr = dummyNext
                if curr:
                    dummyNext = curr.next
                else:
                    break
                    
            
            curr.next = prev
            prev = curr
            curr = dummyNext
            counter += 1
        return prev