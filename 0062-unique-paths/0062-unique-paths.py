class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for _ in range(m - 1):
            row = [1] * n
            for c in range(n - 2, -1, -1):
                row[c] = res[c] + row[c + 1]
            res = row
        return res[0]