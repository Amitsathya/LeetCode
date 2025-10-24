class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        visit = set()
        minH = [[0, k]]
        res = 0
        while minH:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res = max(res, cost)
            visit.add(i)
            for nei, neiCost in edges[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost + cost, nei])
        return res if len(visit) == n else -1