class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in arr.keys():
                return [i,arr[diff]]
            arr[v]=i

            
            