"""
21. 중복 문자 제거
316. remove duplicate letters

Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
* 1 <= s.length <= 10**4
* s consists of lowercase English letters.

Note: This question is the same as 1081:
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

"""
# 내 풀이
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []

        for char in s:
            print(char)
            count[char] -= 1

            if char in stack:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                # 답에서 pop
                print("pop")
                stack.pop()

            stack.append(char)

        return ''.join(stack)


# 풀이 1
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         # 집합으로 정렬
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             # 전체 집합과 접미사 집합이 일치할 때 분리 진행
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''

# 풀이 2
# import collections
#
#
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         counter, seen, stack = collections.Counter(s), set(), []
#
#         print(counter)
#         print(seen)
#         print(stack)
#
#         for char in s:
#             print(seen)
#             counter[char] -= 1
#             if char in seen:
#                 continue
#             # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
#             while stack and char < stack[-1] and counter[stack[-1]] > 0:
#                 seen.remove(stack.pop())
#             stack.append(char)
#             seen.add(char)
#
#         return ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    s = 'bcabc'
    print(sol.removeDuplicateLetters(s))

"""
재귀 

input  s = 'cbacdcbc'


for
['a', 'b', 'c', 'd'] 중 a
set(s)      {'b', 'c', 'd', 'a'}
set(suffix) {'c', 'a', 'd', 'b'} suffix acdcbc
재귀 return a

for
['b', 'c', 'd'] 중 b
set(s)      {'b', 'c', 'd'}
set(suffix) {'b', 'c'} suffix bc
재귀x 반복

for
['b', 'c', 'd'] 중 c
set(s)      {'b', 'c', 'd'}
set(suffix) {'b', 'c', 'd'} suffix cdcbc
재귀 return c

for
['b', 'd'] 중 b
set(s)      {'b', 'd'}
set(suffix) {'b'} suffix b
재귀x 반복

for
['b', 'd'] 중 d
set(s)      {'b', 'd'}
set(suffix) {'b', 'd'} suffix db
재귀 return d

for
['b'] 중 b
set(s)      {'b'}
set(suffix) {'b'} suffix b
재귀 return b

return : acdb


"""
