# https://leetcode.com/problems/sqrtx/description/

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x

        while left <= right:
            mid = math.floor((left + right) / 2)
            
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left  = mid + 1

        return right

def test_case_1() -> None:
    assert Solution().mySqrt(4) == 2

def test_case_2() -> None:
    assert Solution().mySqrt(8) == 2
