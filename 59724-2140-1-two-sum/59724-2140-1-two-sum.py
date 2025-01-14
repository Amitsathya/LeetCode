class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dit.keys():
                return [i, dit[diff]]
            dit[v] = i
        return False

            
            