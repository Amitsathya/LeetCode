class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):


            if amount == 0:
                return 0
            if amount<0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            memo[amount] = min([1+dfs(amount-c) for c in coins])
            return memo[amount]


        minimum = dfs(amount)
        return minimum if minimum < float("inf") else -1
        