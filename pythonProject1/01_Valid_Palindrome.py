"""

유효한 팰린드롬

125. Valid Palindrome
리트코드 출

-------------------------------
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
-------------------------------
* 팰린드롬
앞뒤가 똑같은 문장으로 뒤집어도 똑같ㅌ은 단어 또는 문장을 말함.
"""


# 내 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = True
        ans_check = []
        for i in s:
            if i.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별
                ans_check.append(i.lower()) # lower() : 모두 소문자로 변환

        for i in range(len(ans_check)):
            if ans_check[i] != ans_check[-(i+1)]:
                answer = False
                break

        return answer


solution = Solution()
s = 'A man, a plan, a canal: Panama'
solution.isPalindrome(s)

# answer 1,2,3
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

"""


"""
import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
    
"""


"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱
    
    
"""