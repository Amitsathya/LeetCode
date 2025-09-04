class MedianFinder:

    def __init__(self):
        self.big, self.small = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        if self.small and self.big and self.small[0] * -1 > self.big[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.small) > len(self.big) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.big) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.big)
            heapq.heappush(self.small, val)        

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return self.small[0] * -1
        elif len(self.big) > len(self.small):
            return self.big[0]
        else:
            return (self.small[0] * -1 + self.big[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()