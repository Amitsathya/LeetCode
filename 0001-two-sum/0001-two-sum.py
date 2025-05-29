class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dicts:
                return [i, dicts[diff]]
            dicts[n] = i
        return -1
        