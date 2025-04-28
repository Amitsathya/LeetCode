class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited = set()
        atlantic_visitied = set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if ((row) in range(rows) and (col) in range(cols) and (row, col) not in visited and heights[row][col] >= heights[r][c]):
                    dfs(row, col, visited)
        
        for i in range(rows):
            dfs(0, i, pacific_visited)
            dfs(rows - 1, i, atlantic_visitied)
        
        for j in range(cols):
            dfs(j, 0, pacific_visited)
            dfs(j, cols - 1, atlantic_visitied)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visitied:
                    res.append((r, c))
        return res
        