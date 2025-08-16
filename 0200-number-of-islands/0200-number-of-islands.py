class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[r][c] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
