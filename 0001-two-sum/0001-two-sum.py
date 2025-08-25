class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dicts:
                return [i, dicts[diff]]
            dicts[v] = i
        return -1