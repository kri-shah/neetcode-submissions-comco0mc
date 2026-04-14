class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            m = (l + r) // 2
            print(m)
            sqrt = m * m
            if sqrt < x:
                l = m + 1
            else:
                r = m
        
        return l if l * l <= x else l - 1
