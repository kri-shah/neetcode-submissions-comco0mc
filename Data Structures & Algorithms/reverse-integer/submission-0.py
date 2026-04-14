class Solution:
    def reverse(self, x: int) -> int:
        overflow = 2147483647
        
        is_neg = x < 0
        if is_neg:
            x *= -1

        res = x % 10
        x //= 10
        while x:
            digit = x % 10
            if res > overflow // 10 or (res == overflow and digit > 7):
                return 0
            
            res *= 10
            res += digit
            x //= 10
        
        return -res if is_neg else res