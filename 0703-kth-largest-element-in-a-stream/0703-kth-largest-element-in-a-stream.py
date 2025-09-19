class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.res, self.k = nums, k
        heapq.heapify(self.res)
        while len(self.res) > k:
            heapq.heappop(self.res)

    def add(self, val: int) -> int:
        heapq.heappush(self.res, val)
        while len(self.res) > self.k:
            heapq.heappop(self.res)
        return self.res[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)