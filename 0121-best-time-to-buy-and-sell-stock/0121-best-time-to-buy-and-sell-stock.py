class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for p in prices:
            minBuy = min(minBuy, p)
            maxProfit = max(maxProfit, p - minBuy)
        return maxProfit
        