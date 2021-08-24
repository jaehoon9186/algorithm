"""
06 가장 긴 팰린드롬 부분 문자열
5. Logest Palindrome substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
* 1 <= s.length <= 1000
* s consist of only digits and English letters.

"""

# 내 풀이
# 시간 초과 > 예외처리로 해결
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # 해당 사항이 없을때 빠르게 리턴 < - 이렇게 처리 안하면 시간초과뜸..
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         max_pal = ''
#         for p1 in range(len(s)):
#             for p2 in range(p1, len(s)):
#                 check_str = s[p1:p2+1] # +1 : 이유, 문자열 슬라이싱 할때 p2(인덱스) -1 까지 조회하기때문
#                 # 팰린드롬인지? and 더 큰 팰린드롬 인지?
#                 if check_str[:] == check_str[::-1] and len(check_str) > len(max_pal):
#                     max_pal = check_str
#
#         return max_pal
#
# sol = Solution()
# s = "babad"
# sol.longestPalindrome(s)


# 풀이 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            print('L', left, 'R',right)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        return result

if __name__=="__main__":
    sol = Solution()
    s = "babad"
    print("답:", sol.longestPalindrome(s))
