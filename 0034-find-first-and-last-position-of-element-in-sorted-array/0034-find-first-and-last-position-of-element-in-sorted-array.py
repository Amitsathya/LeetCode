class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLR(left):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    res = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return res
        return [findLR(1), findLR(0)]