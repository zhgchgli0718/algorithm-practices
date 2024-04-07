# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List
import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        foundIndex = -1
        while left <= right:
            index = math.floor((left + right) / 2)
            
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            elif nums[index] == target:
                foundIndex = index
                break
        
        #<<
        startIndex = foundIndex
        while startIndex - 1 >= 0 and nums[startIndex - 1] == target:
            startIndex -= 1

        #>>
        endIndex = foundIndex
        while endIndex + 1 < len(nums) and nums[endIndex + 1] == target:
            endIndex += 1

        return [startIndex, endIndex]


def test_case_1() -> None:
    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4]

def test_case_2() -> None:
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1]

def test_case_3() -> None:
    assert Solution().searchRange([], 0) == [-1,-1]

def test_case_4() -> None:
    assert Solution().searchRange([1,1,2], 1) == [0,1]