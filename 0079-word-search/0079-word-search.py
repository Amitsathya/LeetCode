class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[i] != board[r][c] or (r, c) in visited:
                return
            visited.add((r, c))
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if dfs(i + 1, row, col):
                    return True
            visited.remove((r, c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False