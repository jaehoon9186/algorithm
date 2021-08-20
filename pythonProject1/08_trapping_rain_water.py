"""
08. 빗물 트래핑
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:
* n == height.length
* 1 <= n <= 2 * 10**4
* 0 <= height[i] <= 10**5

"""

# 풀이 1
# from typing import List
#
#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#
#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]
#
#         while left < right:
#             left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#             print(left, right ,left_max, right_max)
#             # 더 높은 쪽을 향해 투 포인터 이동
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -= 1
#         return volume

# 풀이 2
#
# from typing import List
#
#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = []
#         volume = 0
#
#         for i in range(len(height)):
#             # 변곡점을 만나는 경우
#             while stack and height[i] > height[stack[-1]]:
#                 # 스택에서 꺼낸다
#                 top = stack.pop()
#
#                 if not len(stack):
#                     break
#
#                 # 이전과의 차이만큼 물 높이 처리
#                 distance = i - stack[-1] - 1
#                 waters = min(height[i], height[stack[-1]]) - height[top]
#
#                 volume += distance * waters
#
#             stack.append(i)
#         return volume

# 풀이 3 (유튵ㅂ)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0]*n
        right_max = [0]*n

        # 초기 값
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        # 왼쪽부터, 오른쪽부터 높이 별로 max값
        for i in range(1, n): # i > 1 ~ 11
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, -1, -1): # i > 10 ~ 0
            right_max[i] = max(right_max[i+1], height[i])

        answer = 0
        for i in range(n):
            answer += min(left_max[i], right_max[i])-height[i]

        return answer


sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))