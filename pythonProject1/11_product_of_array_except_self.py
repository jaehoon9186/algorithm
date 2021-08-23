"""
11. 자신을 제외한 배열의 곱
238. product of array except self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
* 2 <= nums.length <= 10**5
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

# 내 풀이
# 통과했는데 너무 오래걸림
# from typing import List
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#         mul1 = [1]
#         mul2 = [1]
#         mul = 1
#         for i in rang en(nums)-1):
#             mul = nums[i] * mul
#             mul1.append(mul)
#
#         mul = 1
#         for i in range(len(nums)-1,0,-1):
#             mul = nums[i] * mul
#             mul2.insert(0, mul)  #insert가 시간을 많이 잡아먹나.
#
#         for i in range(len(nums)):
#             answer.append(mul1[i]*mul2[i])
#
#         return answer

# 풀이 1
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))