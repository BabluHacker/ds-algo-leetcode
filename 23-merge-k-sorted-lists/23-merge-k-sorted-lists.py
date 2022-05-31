# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        # print(k)
        if k == 0: return None
        mergeList = lists[0]
        for i in range(1, k):
            # print(mergeList)
            mergeList = self.mergeTwoList(mergeList, lists[i])
        return mergeList
        
    def mergeTwoList(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1= list1.next
                
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
                
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next