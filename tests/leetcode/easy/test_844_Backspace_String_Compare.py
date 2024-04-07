# https://leetcode.com/problems/backspace-string-compare/description/

from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.result(s) == self.result(t)
    
    def result(self, s: str) -> str:
        fastIndex = 0
        slowIndex = 0
        chars = [char for char in s]

        while fastIndex < len(chars):
            if chars[fastIndex] != "#":
                chars[slowIndex] = chars[fastIndex]
                slowIndex += 1
            elif chars[fastIndex] == "#":
                chars[slowIndex] = chars[fastIndex]
                slowIndex -= 1
                if slowIndex < 0:
                    slowIndex = 0
                
            fastIndex += 1
        return chars[0:slowIndex]

def test_case_1() -> None:
    assert Solution().backspaceCompare("ab#c", "ad#c") == True

def test_case_2() -> None:
    assert Solution().backspaceCompare("ab##", "c#d#") == True

def test_case_3() -> None:
    assert Solution().backspaceCompare("y#fo##f", "y#f#o##f") == True

def test_case_4() -> None:
    assert Solution().backspaceCompare("a#c", "b") == False

