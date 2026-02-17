# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.endOfWord = False

# class Solution:
#     def __init__(self):
#         self.root = TrieNode()

#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = []
#         for s in strs:
#             curr = self.root
#             for c in s:
#                 if c not in curr.children:
#                     curr.children[c] = TrieNode()
#                 curr = curr.children[c]
#             curr.endOfWord = True
        
#         def dfs(root):
#             children = root.children.values()
#             if not children and len(children) > 1:
#                 return "".join(res)
#             res.append(children[0])
#             dfs(children[0])
#         return dfs(self.root)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Build trie
        for s in strs:
            curr = self.root
            for c in s:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True

        # Traverse while only one child and not end of word
        res = []
        curr = self.root

        while curr and len(curr.children) == 1 and not curr.endOfWord:
            c, next_node = next(iter(curr.children.items()))
            res.append(c)
            curr = next_node

        return "".join(res)
        

