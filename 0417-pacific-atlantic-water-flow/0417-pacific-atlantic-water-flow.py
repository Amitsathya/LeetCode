class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic_visited, pacific_visited = set(), set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and heights[r][c] <= heights[row][col]:
                    dfs(row, col, visited)
        
        for i in range(ROWS):
            dfs(i, 0, pacific_visited)
            dfs(i, COLS - 1, atlantic_visited)
        
        for j in range(COLS):
            dfs(0, j, pacific_visited)
            dfs(ROWS - 1, j, atlantic_visited)
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in atlantic_visited and (i, j) in pacific_visited:
                    res.append((i, j))
        return res
