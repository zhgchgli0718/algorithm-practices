# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIndex = 0
        fastIndex = 0

        while fastIndex < len(nums):
            if nums[fastIndex] != nums[slowIndex]:
                slowIndex += 1
                nums[slowIndex] = nums[fastIndex]
                
            fastIndex += 1
        
        return slowIndex + 1


def test_case_1() -> None:
    nums = [1,1,2]
    assert Solution().removeDuplicates(nums) == 2
    assert nums[0:2] == [1,2]

def test_case_2() -> None:
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert Solution().removeDuplicates(nums) == 5
    assert nums[0:5] == [0,1,2,3,4]

