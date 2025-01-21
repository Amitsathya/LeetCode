class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in res.keys():
                return [i, res[diff]]
            res[n] = i
        return False
        