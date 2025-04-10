# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head.next : #size 1
            return head

        curr = head
        next, prev = None, None
        count = 0

        for i in range(left - 1):
            prev = curr
            curr = curr.next
            # count += 1

            
        # count = left
        before_start = prev
        prev = None
            
        r1  = self.reverse(curr,(right-left) + 1)

        if before_start:
            before_start.next = r1
        else:
            head = r1

    
        return head

    def reverse (self, head, count):

        curr = head
        next,prev = None,None

        for n in range(count):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = next
        return prev
        
