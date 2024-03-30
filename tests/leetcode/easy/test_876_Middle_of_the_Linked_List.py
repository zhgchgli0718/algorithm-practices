from typing import Optional

# https://leetcode.com/problems/middle-of-the-linked-list/submissions/1218055525/
# two point

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i: Optional[ListNode] = head
        j: Optional[ListNode] = head.next

        while i != None and j != None:
            i = i.next
            j = j.next
            if j != None:
                j = j.next
         

        return i


###
def test_case_1() -> None:
    head: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert Solution().middleNode(head).val == 3

def test_case_2() -> None:
    head: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    assert Solution().middleNode(head).val == 4
