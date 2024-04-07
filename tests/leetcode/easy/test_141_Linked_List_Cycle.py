# https://leetcode.com/problems/linked-list-cycle/
# linked list, two points

from helper.ListNode import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        i: ListNode = head
        j: ListNode = head.next

        while i != None and j != None:
            
            if i == j:
                return True

            i = i.next
            j = j.next
            if j != None:
                j = j.next

        return False
    

def test_case_1():
    listNode3: ListNode = ListNode(3)
    listNode2: ListNode = ListNode(2)
    listNode0: ListNode = ListNode(0)
    listNode_4: ListNode = ListNode(-4)

    listNode3.next = listNode2
    listNode2.next = listNode0
    listNode0.next = listNode_4
    listNode_4.next = listNode2

    assert Solution().hasCycle(listNode3) == True

def test_case_2():
    listNode1: ListNode = ListNode(3)
    listNode2: ListNode = ListNode(2)

    listNode1.next = listNode2
    listNode2.next = listNode1

    assert Solution().hasCycle(listNode1) == True

def test_case_3():
    listNode1: ListNode = ListNode(1)

    assert Solution().hasCycle(listNode1) == False
