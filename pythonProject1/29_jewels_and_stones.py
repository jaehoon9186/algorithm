"""
29. 보석과 돌
771. jewels ans stones
https://leetcode.com/problems/jewels-and-stones/

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0


Constraints:
* 1 <= jewels.length, stones.length <= 50
* jewels and stones consist of only English letters.
* All the characters of jewels are unique.

"""

# 내 풀이


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jew = dict()
        for i in range(len(jewels)):
            jew[jewels[i]] = 0

        for s in range(len(stones)):
            if stones[s] in jew:
                answer += 1

        return answer

# 풀이 1
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = {}
#         count = 0
#
#         # 돌(S)의 빈도 수 계산
#         for char in S:
#             if char not in freqs:
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1
#
#         # 보석(J)의 빈도 수 합산
#         for char in J:
#             if char in freqs:
#                 count += freqs[char]
#
#         return count

# 풀이 2
# import collections
#
#
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = collections.defaultdict(int)
#         count = 0
#
#         # 비교 없이 돌(S) 빈도 수 계산
#         for char in S:
#             freqs[char] += 1
#
#         # 비교 없이 보석(J) 빈도 수 합산
#         for char in J:
#             count += freqs[char]
#
#         return count

# 풀이 3
# import collections
#
#
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
#         count = 0
#
#         # 비교 없이 보석(J) 빈도 수 합산
#         for char in J:
#             count += freqs[char]
#
#         return count


# 풀이 4
#
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         return sum(s in J for s in S)


if __name__ == "__main__":
    sol = Solution()
    j = "aA"
    s = "aAAbbbb"
    print(sol.numJewelsInStones(j, s))