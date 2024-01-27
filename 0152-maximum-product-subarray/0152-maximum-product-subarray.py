class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tempMax = n * curMax
            curMax = max(tempMax, n * curMin, n)
            curMin = min(tempMax, n * curMin, n)
            res = max(curMax, res, curMin)
        return res
        