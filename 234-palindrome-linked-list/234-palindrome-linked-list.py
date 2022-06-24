# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        
        def recur_check(head):
            if not head:
                return True
            # valid node
            last = recur_check(head.next)
            val = self.front.val
            self.front = self.front.next
            if not last or head.val != val:
                
                return False
            else:
                return True
        return recur_check(head)
                
                