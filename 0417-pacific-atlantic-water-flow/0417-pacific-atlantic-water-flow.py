class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0],[0, 1], [0, -1],[1, 0]]
        atlanticVisited = set()
        pacificVisited = set()

        def bfs(r, c, vist):
            q = deque([(r, c)])
            vist.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in vist:
                            q.append((nr, nc))
                            vist.add((nr, nc))
        
        for i in range(ROWS):
            bfs(i, 0, pacificVisited)
            bfs(i, COLS - 1, atlanticVisited)
        
        for j in range(COLS):
            bfs(0, j, pacificVisited)
            bfs(ROWS - 1, j, atlanticVisited)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlanticVisited and (r, c) in pacificVisited:
                    res.append((r, c))
        return res  