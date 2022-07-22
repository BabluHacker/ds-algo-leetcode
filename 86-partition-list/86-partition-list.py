# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        part1 = partHead1 = ListNode(0)
        part2 = partHead2 = ListNode(0)
        
        
        curr = head
        while curr:
            if curr.val < x:
                part1.next = ListNode(curr.val)
                part1 = part1.next
            else:
                part2.next = ListNode(curr.val)
                part2 = part2.next
                
            curr = curr.next 
            
        part1.next = partHead2.next
        
        return partHead1.next
        
    