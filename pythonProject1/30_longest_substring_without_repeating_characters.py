"""
30. 중복 문자 없는 가장 긴 부분 문자열
3. Longest Substring without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0


Constraints:
* 0 <= s.length <= 5 * 10^4
* s consists of English letters, digits, symbols and spaces.

"""


# 내 풀이
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         max_s = ''
#
#         for i in range(len(s)):
#             j = i
#             count_s = ''
#             while j < len(s) and s[j] not in count_s:
#                 count_s = count_s + s[j]
#                 if len(count_s) > len(max_s):
#                     max_s = count_s
#                 j = j + 1
#
#         return len(max_s)

# 풀이 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length

if __name__ == "__main__":
    sol = Solution()
    s = 'pwwkew'
    print(sol.lengthOfLongestSubstring(s))
