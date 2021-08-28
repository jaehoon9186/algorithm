"""
22. 일일 온도
739. daily temperatures
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the i**th day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
* 1 <= temperatures.length <= 10**5
* 30 <= temperatures[i] <= 100

"""


# 내 풀이
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack =[]
        answer = [0]*len(temperatures)

        for i, val in enumerate(temperatures):
            print(i, val)
            while stack and val > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)


        return answer

# 풀이 1
#
# from typing import List
#
#
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         answer = [0] * len(T)
#         stack = []
#         for i, cur in enumerate(T):
#             # 현재 온도가 스택 값보다 높다면 정답 처리
#             while stack and cur > T[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)
#
#         return answer


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))
