class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # If left portion is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # Target is within left portion
                    r = mid - 1
                else:
                    l = mid + 1

            # Right portion is sorted
            else:
                if nums[mid] < target <= nums[r]:  # Target is within right portion
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
        