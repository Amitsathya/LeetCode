class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]
        for p in prices[1:]:
            bought = min(bought, p)
            profit = max(profit, p - bought)
        return profit