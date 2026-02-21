class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum4 > target:
                        r -= 1
                    elif sum4 < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res