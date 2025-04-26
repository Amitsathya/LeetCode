class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if (
                    0 <= new_r < len(heights) and
                    0 <= new_c < len(heights[0]) and
                    (new_r, new_c) not in visited and
                    heights[new_r][new_c] >= heights[r][c]
                ):
                    dfs(new_r, new_c, visited)
        # Top row (Pacific)
        for c in range(len(heights[0])):
            dfs(0, c, pacific_reachable)

        # Left column (Pacific)
        for r in range(len(heights)):
            dfs(r, 0, pacific_reachable)

        # Bottom row (Atlantic)
        for c in range(len(heights[0])):
            dfs(len(heights)-1, c, atlantic_reachable)

        # Right column (Atlantic)
        for r in range(len(heights)):
            dfs(r, len(heights[0])-1, atlantic_reachable)
        
        result = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        return result


