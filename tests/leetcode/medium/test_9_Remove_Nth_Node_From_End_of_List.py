from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i: ListNode = head
        j: ListNode = head
        
        count = 1
        while count <= n:
            j = j.next
            count += 1

        prev = i
        while i != None and j != None :
            prev = i
            i = i.next
            j = j.next
        
        if prev == i:
            return prev.next

        prev.next = i.next

        return head
    


###
            
def listnode_to_array(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array

def test_case_1() -> None:
    head: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert listnode_to_array(Solution().removeNthFromEnd(head, 2)) == [1,2,3,5]

def test_case_2() -> None:
    head: ListNode = ListNode(1)
    assert listnode_to_array(Solution().removeNthFromEnd(head, 1)) == []

def test_case_3() -> None:
    head: ListNode = ListNode(1, ListNode(2))
    assert listnode_to_array(Solution().removeNthFromEnd(head, 1)) == [1]

def test_case_4() -> None:
    head: ListNode = ListNode(1, ListNode(2))
    assert listnode_to_array(Solution().removeNthFromEnd(head, 2)) == [2]