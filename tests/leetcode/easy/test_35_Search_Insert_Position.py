# https://leetcode.com/problems/search-insert-position/description/

from typing import List
import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = math.floor((left + right) / 2)

            if nums[index] > target:
                # 在左邊
                right = index - 1
            elif nums[index] < target:
                # 在右邊
                left = index + 1
            elif nums[index] == target:
                return index
        return left

def test_case_1() -> None:
    assert Solution().searchInsert([1,3,5,6], 5) == 2

def test_case_2() -> None:
    assert Solution().searchInsert([1,3,5,6], 2) == 1

def test_case_3() -> None:
    assert Solution().searchInsert([1,3,5,6], 7) == 4
