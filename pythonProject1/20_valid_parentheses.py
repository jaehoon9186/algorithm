"""
20. 유효한 괄호
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true


Constraints:
* 1 <= s.length <= 10**4
* s consists of parentheses only '()[]{}'
"""


# 내 풀이

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pop_list = ['()','[]','{}']

        answer = bool

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1:
                if ''.join([stack[-2], stack[-1]]) in pop_list:
                    stack.pop()
                    stack.pop()

        if len(stack) == 0:
            answer = True
        else:
            answer = False

        return answer

# 풀이 1
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         table = {
#             ')': '(',
#             '}': '{',
#             ']': '[',
#         }
#
#         # 스택 이용 예외 처리 및 일치 여부 판별
#         for char in s:
#             if char not in table:
#                 stack.append(char)
#             elif not stack or table[char] != stack.pop():
#                 return False
#
#         return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    s = '()'
    print(sol.isValid(s))
