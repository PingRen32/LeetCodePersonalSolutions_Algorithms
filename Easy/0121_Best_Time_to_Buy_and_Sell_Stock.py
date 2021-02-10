# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dim = len(prices)

        if dim == 0:
            return 0

        minval, res = prices[0], 0

        for i in range(dim):
            if prices[i] < minval:
                minval = prices[i]
            elif prices[i] - minval > res:
                res = prices[i] - minval

        return res
    