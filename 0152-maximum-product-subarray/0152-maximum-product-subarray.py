class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        for n in  nums:
            if n == 0:
                currMin, currMax = 1, 1
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(currMin * n, temp, n)
            res = max(currMax, res)
        return res