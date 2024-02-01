class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helperRob(nums[:-1]), self.helperRob(nums[1:]), nums[0])        
        
    def helperRob(self, n):
        rob1, rob2 = 0, 0
        for n in n:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        