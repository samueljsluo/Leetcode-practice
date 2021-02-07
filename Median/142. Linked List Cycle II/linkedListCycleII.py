# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # fast = slow = head
        # while fast != None and fast.next != None:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast==slow:
        #         break
        # else:
        #     return None
        # while slow!=head:
        #     slow = slow.next
        #     head = head.next
        # return head
        
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                break
        
        if fast is None or fast.next is None: return None
        
        while slow != head:
            head = head.next
            slow = slow.next
        return head
    