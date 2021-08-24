"""
07. 두 수의 합
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""
# 내 풀이
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        breaker = False

        for p1 in range(len(nums)):
            for p2 in range(p1+1, len(nums)):
                if nums[p1] + nums[p2] == target:
                    answer.append(p1)
                    answer.append(p2)
                    breaker = True
                if breaker:
                    break
            if breaker:
                break

        return answer

if __name__=="__main__":
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    sol.twoSum(nums, target)


# 풀이 1
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# 풀이 2
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums): # enumerate(nums) > 인덱스, 값  리턴
#             complement = target - n
#
#             if complement in nums[i + 1:]: # 타겟에서 현재 값을 뺀 값(A)이 다음 배열안에 있는 경우(B) A+B = target
#                 return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# 풀이 3
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         # 키와 값을 바꿔서 딕셔너리로 저장
#         for i, num in enumerate(nums):
#             nums_map[num] = i
#
#         # > {2: 0, 7: 1, 11: 2, 15: 3}
#
#         # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#         for i, num in enumerate(nums):
#             # if 타겟에서 현재값을 뺀값이 in nums_map에 key값이랑 같을때
#             # and index값이 동일하지 않은 경우
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return [i, nums_map[target - num]]

# 풀이 4
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         # 하나의 `for`문으로 통합
#         for i, num in enumerate(nums):
#             if target - num in nums_map:
#                 return [nums_map[target - num], i]
#             nums_map[num] = i

# 풀이 5
# 투포인터로 풀려면 정렬 필요, 정렬하게되면 index 값을 찾기 힘듬.
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         left, right = 0, len(nums) - 1
#         while not left == right:
#             # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
#             if nums[left] + nums[right] < target:
#                 left += 1
#             # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
#             elif nums[left] + nums[right] > target:
#                 right -= 1
#             else:
#                 return [left, right]



# sol = Solution()
# nums = [2,7,11,15]
# target = 9
# print(sol.twoSum(nums, target))