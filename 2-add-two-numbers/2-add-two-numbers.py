# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = ListNode()
        tmp = resultHead
        curr1 = l1
        curr2 = l2
        s, c = 0, 0
        while (curr1 or curr2):
            d1, d2 = 0, 0
            if curr1:
                d1 = curr1.val
                curr1 = curr1.next
            if curr2:
                d2 = curr2.val
                curr2 = curr2.next
            s = d1 + d2 + c
            c = s // 10
            # print(d1, d2)
            tmp.next = ListNode(s%10)
            tmp = tmp.next
            
        # print(c)
        if c != 0:
            tmp.next = ListNode(c)
        return resultHead.next
            