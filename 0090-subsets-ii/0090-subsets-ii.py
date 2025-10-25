class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backTrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backTrack(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backTrack(i + 1, curr)
        backTrack(0, [])
        return res