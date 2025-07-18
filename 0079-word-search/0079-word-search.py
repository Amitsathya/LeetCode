class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if  i == len(word):
                return True
            if  r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            
            path.add((r, c))
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if dfs(row, col, i + 1):
                    return True
            path.remove((r, c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False