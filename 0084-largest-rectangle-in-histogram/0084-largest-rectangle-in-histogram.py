class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        resMax = 0 
        res = []
        for i, h in enumerate(heights):
            start = i
            while res and res[-1][1] > h:
                index, height = res.pop()
                resMax = max(resMax, height * (i - index))
                start = index
            res.append([start, h])
        for i, h in res:
            resMax = max(resMax, h * (len(heights) - i))
        return resMax