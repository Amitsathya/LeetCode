class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0],[0, 1], [0, -1],[1, 0]]
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            res = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1 and (r, c) not in visited:
                            q.append((r, c))
                            visited.add((r, c))
                            res += 1
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res
        