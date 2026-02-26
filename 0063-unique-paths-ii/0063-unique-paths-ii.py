class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # res = 
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        res = [[0] * (n + 1) for _ in range(m + 1)]
        res[m - 1][n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    res[r][c] = 0
                else:
                    res[r][c] += res[r + 1][c] + res[r][c + 1]
        # print(res)
        return res[0][0]
        # return 2
        # for r in 