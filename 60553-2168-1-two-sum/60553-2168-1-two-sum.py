class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, v in enumerate(nums):
            diff= target- v
            if diff in pos.keys():
                return [i, pos[diff]]
            pos[v] = i
        return -1
            
        