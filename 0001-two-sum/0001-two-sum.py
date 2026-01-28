class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in req.keys():
                return [i, req[diff]]
            req[n] = i
        return [-1, -1]