# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slowIndex = 0
        fastIndex = 0

        while fastIndex < len(nums):
            if nums[fastIndex] != 0:
                slow = nums[slowIndex]
                nums[slowIndex] = nums[fastIndex]
                nums[fastIndex] = slow
                slowIndex += 1
            fastIndex += 1
        


def test_case_1() -> None:
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    assert nums == [1,3,12,0,0]

def test_case_2() -> None:
    nums = [0]
    Solution().moveZeroes(nums)
    assert nums == [0]

