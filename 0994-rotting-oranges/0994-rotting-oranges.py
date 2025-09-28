class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = set()
        good = set()
        q = deque()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def turnIntoRotten(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in rotten or (r, c) not in good):
                return
            rotten.add((r, c))
            q.append((r, c))
            good.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    good.add((r, c))
        time = -1
        while q:
            for _ in range(len(q)):
                r, c  = q.popleft()
                for dr, dc in directions:
                    turnIntoRotten(r + dr, c + dc)
            time += 1
        return max(time, 0) if len(good) == 0 else -1


        