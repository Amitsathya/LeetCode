class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(currMin *n, temp, n)
            res = max(res, currMax)
        return res
        