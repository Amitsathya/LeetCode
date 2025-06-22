class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        atlantic_visited = set()
        pacific_visited = set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < rows and 0 <= col < cols and (row, col) not in visited and heights[row][col] >= heights[r][c]):
                    dfs(row, col, visited)
        
        for i in range(cols):
            dfs(0, i, pacific_visited)
            dfs(rows - 1, i, atlantic_visited)
        
        for j in range(rows):
            dfs(j, 0, pacific_visited)
            dfs(j, cols - 1, atlantic_visited)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    res.append((r, c))
        return res