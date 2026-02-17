class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in res:
                return [i, res[diff]]
            res[v] = i
        return [-1, -1]