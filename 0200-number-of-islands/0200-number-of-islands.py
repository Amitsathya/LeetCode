class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                r, c = queue.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == "1":
                        queue.append((row, col))
                        visited.add((row, col))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands