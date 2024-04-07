# https://leetcode.com/problems/binary-search/

from typing import List
import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        return -1

def test_case_1() -> None:
    assert Solution().search([-1,0,3,5,9,12], 9) == 4

def test_case_2() -> None:
    assert Solution().search([-1,0,3,5,9,12], 2) == -1
