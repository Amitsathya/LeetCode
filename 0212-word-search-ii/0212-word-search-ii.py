class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children or (r, c) in visit:
                return
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, word, node)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)
        