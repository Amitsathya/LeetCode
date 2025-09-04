class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for p in prices[1:]:
            buy = min(p, buy)
            profit = max(profit, p - buy)
        return profit