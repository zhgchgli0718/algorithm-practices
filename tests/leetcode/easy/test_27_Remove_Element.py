# https://leetcode.com/problems/remove-element/description/


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex = 0
        fastIndex = 0

        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
            fastIndex += 1

        return slowIndex

def test_case_1() -> None:
    nums = [3,2,2,3]
    assert Solution().removeElement(nums, 3) == 2
    assert nums[0:2] == [2,2]

def test_case_2() -> None:
    nums = [0,1,2,2,3,0,4,2]
    assert Solution().removeElement(nums, 2) == 5
    assert nums[0:5] == [0,1,3,0,4]

