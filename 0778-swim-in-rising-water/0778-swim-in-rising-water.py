class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set([0, 0])
        minH = [[grid[0][0], 0, 0]]
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nc < 0 or nr < 0 or nr == N or nc == N or (nr, nc) in visit:
                    continue
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
                visit.add((nr, nc))
        return 0

