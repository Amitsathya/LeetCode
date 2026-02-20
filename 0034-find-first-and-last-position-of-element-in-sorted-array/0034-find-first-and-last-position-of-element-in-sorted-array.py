class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(left):
            res = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r)// 2
                if nums[m] == target:
                    res = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return res
        return [find(1), find(0)]