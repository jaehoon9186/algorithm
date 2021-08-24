"""
12. 주식을 사고팔기 가장 좋은 시점
121. best time to buy and sell stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the i**th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
* 1 <= prices.length <= 10**5
* 0 <= prices[i] <= 10**4

"""

# 내 풀이
# from typing import List
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         answer = 0
#         min = prices[0]
#         for i in range(1, len(prices)):
#             if prices[i] < min:
#                 min = prices[i]
#             if prices[i-1] < prices[i]:
#                 answer = max(answer, prices[i] - min)
#
#         return answer


# 풀이 1
# from typing import List
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_price = 0
#
#         for i, price in enumerate(prices):
#             for j in range(i, len(prices)):
#                 max_price = max(prices[j] - price, max_price)
#
#         return max_price

# 풀이 2
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


if __name__=="__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))