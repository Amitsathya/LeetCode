class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextDp = set()
            for t in dp:
                nextDp.add(t)
                nextDp.add(t + nums[i])
                if t == target: return True
            dp = nextDp
        return False