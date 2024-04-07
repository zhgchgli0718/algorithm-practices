# https://leetcode.com/problems/reverse-linked-list/
# linked list, recursive

from helper.ListNode import ListNode
from helper.Helper import Helper
from typing import Optional

class Solution:
    # 遞迴法
    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        reversedHead = self.reverseList_1(head.next)
        head.next.next = head
        head.next = None

        return reversedHead
    
    # 雙(三)指針法
    def reverseList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        prev = None
        curr = head

        while curr != None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next


        return prev
    
    # 頭插法
    def reverseList_3(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if head == None:
            return None
        
        orgHead = head # 1
        curr = head.next # 2
        while curr != None:
            currHead = head # 1
            next = curr.next # 3
            
            head = curr # 2
            curr.next = currHead #1
            orgHead.next = next # 3

            curr = next


        return head
        

###
def test_case_1() -> None:
    assert Helper.listNode_to_array(Solution().reverseList_1(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) == [5,4,3,2,1]
    assert Helper.listNode_to_array(Solution().reverseList_2(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) == [5,4,3,2,1]
    assert Helper.listNode_to_array(Solution().reverseList_3(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) == [5,4,3,2,1]

def test_case_2() -> None:
    assert Helper.listNode_to_array(Solution().reverseList_1(ListNode(1, ListNode(2)))) == [2, 1]
    assert Helper.listNode_to_array(Solution().reverseList_2(ListNode(1, ListNode(2)))) == [2, 1]
    assert Helper.listNode_to_array(Solution().reverseList_3(ListNode(1, ListNode(2)))) == [2, 1]

def test_case_3() -> None:
    assert Helper.listNode_to_array(Solution().reverseList_1(None)) == []
    assert Helper.listNode_to_array(Solution().reverseList_2(None)) == []
    assert Helper.listNode_to_array(Solution().reverseList_3(None)) == []