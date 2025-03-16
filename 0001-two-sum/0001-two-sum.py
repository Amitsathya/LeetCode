class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            res = target - n
            if res in diff.keys():
                return [i, diff[res]]
            diff[n] = i
        return  -1
        