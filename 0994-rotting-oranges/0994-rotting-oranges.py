class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        while fresh != 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1