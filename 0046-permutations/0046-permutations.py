class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backTrack():
            if len(sol) == n:
                ans.append(sol.copy())
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backTrack()
                    sol.pop()
        backTrack()
        return ans