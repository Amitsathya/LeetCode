class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProd, minProd = 1, 1

        for n in nums:
            if n == 0:
                maxProd, minProd = 1, 1
            temp = maxProd *n
            maxProd = max(temp, minProd * n, n)
            minProd = min(temp, minProd * n, n)
            res = max(res, maxProd)
        return res
