# https://leetcode.com/problems/valid-perfect-square/description/

import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        
        left = 1
        right = num

        while left <= right:
            mid = math.floor((left + right) / 2)
            
            if mid == num / mid:
                return True
            elif mid > num / mid:
                right = mid - 1
            else:
                left  = mid + 1

        return False

def test_case_1() -> None:
    assert Solution().isPerfectSquare(16) == True

def test_case_2() -> None:
    assert Solution().isPerfectSquare(14) == False
