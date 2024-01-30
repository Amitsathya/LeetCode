class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in arr.keys():
                return [arr[diff], i]
            arr[n] = i
        