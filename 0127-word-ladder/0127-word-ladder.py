class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j + 1:]
                nei[pattern].append(w)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j + 1:]
                    for neiW in nei[pattern]:
                        if neiW not in visit:
                            visit.add(neiW)
                            q.append(neiW)
            res += 1
        return 0