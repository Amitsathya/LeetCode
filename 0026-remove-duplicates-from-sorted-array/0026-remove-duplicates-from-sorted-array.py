class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1  # position to write the next unique value

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write