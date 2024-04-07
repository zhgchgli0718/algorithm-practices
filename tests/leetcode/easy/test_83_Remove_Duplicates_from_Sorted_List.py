# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# linked list

from helper.Helper import Helper
from helper.ListNode import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head

        while pre != None:
            if pre.next != None and pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        
        return head


    

def test_case_1():
    assert Helper.listNode_to_array(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))) == [1,2]

def test_case_2():
    assert Helper.listNode_to_array(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))) == [1,2,3]

def test_case_3():
    assert Helper.listNode_to_array(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(1))))) == [1]