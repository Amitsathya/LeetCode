class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visits = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            visits.add((r, c))
            queue.append((r, c))

            while queue:                
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r,c) not in visits):
                        queue.append((r, c))
                        visits.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visits:
                    bfs(r,c)
                    islands += 1
        return islands