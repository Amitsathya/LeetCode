class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                i = heapq.heappop(heap)
                if i + 1 != 0:
                    q.append([i + 1, time + n])
            if q and q[0][1] == time:                    
                heapq.heappush(heap, q.popleft()[0])
        return time
            
