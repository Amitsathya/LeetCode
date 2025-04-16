class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            sub = target - n
            if sub in diff.keys():
                return [i, diff[sub]]
            diff[n] = i
        return -1

        