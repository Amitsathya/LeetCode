class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minH = [(0, k)]  # (current_time, node)
        visit = set()
        res = 0

        while minH:
            w, i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            res = max(res, w)
            for nei, neiCost in edges[i]:
                if nei not in visit:
                    heapq.heappush(minH, (w + neiCost, nei))

        return res if len(visit) == n else -1
