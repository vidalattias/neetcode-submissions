# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        s = []
        while head != None:
            s.append(head.val)
            head = head.next
        
        print(f'{s=}')
        new_head = ListNode(val=s.pop())
        origin = new_head

        while s:
            new_list = ListNode(val=s.pop())
            new_head.next = new_list
            new_head = new_list
        
        return origin