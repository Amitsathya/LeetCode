class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited, atlantic_visited = set(), set()
        res = []

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and  heights[r][c] <= heights[row][col]:
                    dfs(row, col, visited)
        for i in range(ROWS):
            dfs(i, 0, pacific_visited)
            dfs(i, COLS - 1, atlantic_visited)
        for j in range(COLS):
            dfs(0, j, pacific_visited)
            dfs(ROWS - 1, j, atlantic_visited)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic_visited and (r, c) in pacific_visited:
                    res.append((r, c))
        return res