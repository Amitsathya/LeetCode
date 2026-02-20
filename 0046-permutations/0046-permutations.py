class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backTrack():
            if len(sol) == n:
                res.append(sol.copy())
                return 
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backTrack()
                    sol.pop()
        backTrack()
        return res