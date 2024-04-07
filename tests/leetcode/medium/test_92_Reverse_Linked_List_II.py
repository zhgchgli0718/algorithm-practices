# https://leetcode.com/problems/reverse-linked-list-ii/description/
# linked list

import sys
from helper.ListNode import ListNode
from helper.Helper import Helper
from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newHead: ListNode = ListNode(None, head)
        
        prevNode: ListNode = newHead # None
        currNode: ListNode = newHead.next # 1
        
        count = 1
        while count < left: # 1
            prevNode = currNode
            # 1

            currNode = currNode.next
            # 2

            count += 1

        # prevNode = 1
        # currNode = 2

        node = prevNode # 1
        print("====")
        while count <= right: # 3
            nextNode = currNode.next

            print(currNode.val, prevNode.val, nextNode.val)
            

            currNode.next = prevNode

            prevNode = currNode
            currNode = nextNode

            count += 1

        node.next.next = currNode
        node.next = prevNode
        return newHead.next
    

###
def test_case_1():
    assert Helper.listNode_to_array(Solution().reverseBetween(ListNode(1 , ListNode(2 , ListNode(3, ListNode(4, ListNode(5))))), 2, 4)) == [1,4,3,2,5]


# def test_case_2():
#     assert Helper.listNode_to_array(Solution().reverseBetween(ListNode(5), 1, 1)) == [5]
