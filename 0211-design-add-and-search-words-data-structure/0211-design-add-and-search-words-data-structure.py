class TreeNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    children = root.children.values()
                    for child in children:
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.endOfWord
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)