class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        minH = [-c for c in counts.values()]
        heapq.heapify(minH)
        q = deque()
        t = 0
        while minH or q:
            t += 1
            if minH:
                i = heapq.heappop(minH)
                if i + 1 != 0:
                    q.append([i + 1, t + n])
            if q and q[0][1] == t:
                heapq.heappush(minH, q.popleft()[0])
        return t