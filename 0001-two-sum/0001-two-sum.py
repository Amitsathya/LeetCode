class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapped:
                return [i, mapped[diff]]
            mapped[n] = i
        return -1