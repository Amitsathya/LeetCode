class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        adj = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j + 1:]
                adj[pattern].append(w)
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j + 1:]
                    for w1 in adj[pattern]:
                        if w1 not in visit:
                            q.append(w1)
                            visit.add(w1)            
            res += 1
        return 0