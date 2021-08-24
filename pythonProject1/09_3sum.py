"""
09 세 수의 합
15. 3Sum
https://leetcode.com/problems/3sum/

 Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []


Constraints:
* 0 <= nums.length <= 3000
* -10**5 <= nums[i] <= 10**5

"""
# 내 풀이
# 시간 초과 ..
# from typing import List
#
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         if not nums:
#             return answer
#
#         for i in range(len(nums) - 2):
#             target = 0 - nums[i]
#             print('타겟', target)
#             for j in range(i + 1, len(nums) - 1):
#                 complement = target - nums[j]
#                 print('compl', complement)
#                 if complement in nums[j + 1:]:
#                     answer.append(sorted([nums[i], nums[j], complement]))
#
#         # 중복값 제거 이중 리스트여서 set으로 중복 제거하기 위해서는 tuple로 변환해줘야함
#         answer = list(set(map(tuple, answer)))
#
#         return answer

# 풀이 1
# 시간초과 뜸..
# from typing import List
#
#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         nums.sort()
#
#         # 브루트 포스 n^3 반복
#         for i in range(len(nums) - 2):
#             # 중복된 값 건너뛰기
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, len(nums) - 1):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 for k in range(j + 1, len(nums)):
#                     if k > j + 1 and nums[k] == nums[k - 1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         results.append([nums[i], nums[j], nums[k]])
#
#         return results


# 풀이 2
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # `sum = 0`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # total 0이므로 left right 하나씩 이동  중복제거하고 0이 확적된 상황이라 한쪽만 이동해도 의미 없음.
                    left += 1
                    right -= 1

        return results

if __name__=="__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))