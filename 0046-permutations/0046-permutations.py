class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        def permute():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    permute()
                    sol.pop()
        permute()
        return res