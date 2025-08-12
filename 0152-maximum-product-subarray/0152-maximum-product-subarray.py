class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            temp = curMax * n
            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(curMax, res)
        return res