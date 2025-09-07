class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
            temp = currMax * n
            currMax = max(temp, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            res = max(res, currMax)
        return res