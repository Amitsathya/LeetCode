class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) == 0: return 0
        res = 0
        
        root = Trie()
        for num in arr2:
            node = root
            for digit in str(num):
                if digit not in node.children:
                    node.children[digit] = Trie()
                node = node.children[digit]
            node.isEnd = True
        
        for n in arr1:
            count = 0
            node = root
            for c in str(n):
                if c in node.children:
                    count += 1
                    node = node.children[c]
                else:
                    break
            res = max(res, count)
        return res


        