class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]
        for p in prices[1:]:
            profit = max(profit, p - bought)
            bought = min(bought, p)
        return profit