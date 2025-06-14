class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions =[[-1, 0 ], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(c in range(COLS) and r in range(ROWS) and (r, c) not in visited and grid[r][c] == "1" ):
                        q.append((r, c))
                        visited.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands