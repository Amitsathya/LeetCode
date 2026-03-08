class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def dfs(r, c):
            if 0 > r or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(dr +r, dc + c)
    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)
        # print(board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
