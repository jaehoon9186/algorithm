"""
10 배열파티션 I
561. Array Partition I
https://leetcode.com/problems/array-partition-i/

Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

Example 2:
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6).
min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.


Constraints:
* 1 <= n <= 10**4
* nums.length == 2 * n
* -10**4 <= nums[i] <= 10**4
"""
# 내풀이
# from typing import List
#
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         answer = 0
#         nums.sort()
#         print(nums)
#         for i in range(1, len(nums),2):
#             answer += min(nums[i-1],nums[i])
#         return answer

# 풀이 1
# from typing import List
#
#
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         pair = []
#         nums.sort()
#
#         for n in nums:
#             # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []
#
#         return sum

# 풀이 2
# from typing import List
#
#
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         nums.sort()
#
#         for i, n in enumerate(nums):
#             # 짝수 번째 값의 합 계산
#             if i % 2 == 0:
#                 sum += n
#
#         return sum


# 풀이 3
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__=="__main__":
    sol = Solution()
    nums = [1,4,3,2]
    print(sol.arrayPairSum(nums))