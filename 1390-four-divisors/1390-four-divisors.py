class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            divisors = set()
            for i in range(1, floor(sqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(n // i)
                    divisors.add(i)
            if len(divisors) == 4:
                res += sum(divisors)
        return res