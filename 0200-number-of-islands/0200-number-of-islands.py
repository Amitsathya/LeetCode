class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r >= 0 and r < ROWS and c >=0 and c < COLS and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c)not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands