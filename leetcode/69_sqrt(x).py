class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x // 2

        if x == 1:
            return 1

        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
            elif m * m == x:
                return m
            
        return r