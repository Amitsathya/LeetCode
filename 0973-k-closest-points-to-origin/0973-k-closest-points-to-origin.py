class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x, y in points:
            dist = x**2 + y ** 2
            heapq.heappush(minH, [dist, x, y])
        res = []
        while len(res) != k:
            _, x, y = heapq.heappop(minH)
            res.append((x, y))
        return res