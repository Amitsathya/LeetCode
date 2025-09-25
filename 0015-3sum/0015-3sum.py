class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if v > 0:
                break
            
            if  i > 0 and nums[i - 1] == v:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                diff = nums[l] + nums[r] + v
                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], v])
                    l, r = l + 1, r - 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res
            