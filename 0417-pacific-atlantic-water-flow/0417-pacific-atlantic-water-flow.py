class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pacific_visit = set()
        atlantic_visit = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < len(heights) and 0 <= col < len(heights[0]) and (row, col) not in visited and heights[r][c] <= heights[row][col]):
                    dfs(row, col, visited)
        
        for i in range(len(heights[0])):
            dfs(0, i, pacific_visit)
            dfs(len(heights) - 1, i, atlantic_visit)

        for i in range(len(heights)):
            dfs(i, 0, pacific_visit)
            dfs(i, len(heights[0]) - 1, atlantic_visit)
        res = []
        for r  in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific_visit and (r, c) in atlantic_visit:
                    res.append((r, c))
        return res

        