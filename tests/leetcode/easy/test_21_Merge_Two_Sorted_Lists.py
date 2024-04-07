# https://leetcode.com/problems/merge-two-sorted-lists/description/
# linked list

from helper.Helper import Helper
from helper.ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1Head = list1
        list2Head = list2

        result = ListNode()
        pre = result
        while list1Head != None and list2Head != None:
            if list1Head.val < list2Head.val:
                pre.next = list1Head
                pre = list1Head
                list1Head = list1Head.next
            else:
                pre.next = list2Head
                pre = list2Head
                list2Head = list2Head.next

        pre.next = list1Head or list2Head
        
        return result.next

    

def test_case_1():
    assert Helper.listNode_to_array(Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))) == [1,1,2,3,4,4]

def test_case_2():
    assert Helper.listNode_to_array(Solution().mergeTwoLists(None, None)) == []

def test_case_3():
    assert Helper.listNode_to_array(Solution().mergeTwoLists(None, ListNode(0))) == [0]
