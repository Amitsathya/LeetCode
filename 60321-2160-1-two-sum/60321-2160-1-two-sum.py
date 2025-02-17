class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pos.keys():
                return [i, pos[diff]]
            pos[n] = i
        return False
        