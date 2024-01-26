class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            temp =  min(cost[i + 1], cost[i + 2])
            cost[i] += temp
        return min(cost[0], cost[1])
        
        