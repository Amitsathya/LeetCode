class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            val = abs(stone1 - stone2)
            if val >= 1:
                heapq.heappush(stones, val * -1)
        stones.append(0)
        return stones[0] * -1