class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in arr:
                return [i, arr[diff]]
            arr[n] = i
        return arr
            
            