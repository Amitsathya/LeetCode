class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque() #index, timestamp
        time = 0
        while q or maxHeap:
            time += 1
            if maxHeap:
                i = heapq.heappop(maxHeap)
                if i + 1 != 0:
                    q.append([i + 1, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            