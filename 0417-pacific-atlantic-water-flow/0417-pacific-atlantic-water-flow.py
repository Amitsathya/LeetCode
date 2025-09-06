class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlanticVisited, pacificVisited = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)
        
        for i in range(ROWS):
            dfs(i, 0, pacificVisited)
            dfs(i, COLS - 1, atlanticVisited)

        for j in range(COLS):
            dfs(0, j, pacificVisited)
            dfs(ROWS - 1, j, atlanticVisited)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificVisited and (r, c) in atlanticVisited:
                    res.append((r, c))
        return res