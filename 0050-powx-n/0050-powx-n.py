class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = - n
        
        def pow(x, n):
            if n == 0:
                return 1
            half_pow = pow(x, n // 2)
            if n % 2 == 0:
                return half_pow * half_pow
            else:
                return half_pow * half_pow * x
        return pow(x, n)
