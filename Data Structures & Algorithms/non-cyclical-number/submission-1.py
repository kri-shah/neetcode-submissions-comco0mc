class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(num):
            res = 0
            while num:
                digit = num % 10
                num //= 10
                res += digit ** 2
            
            return res
        
        slow = n
        fast = digit_sum(n)

        while slow != fast and fast != 1:
            slow = digit_sum(slow)
            fast = digit_sum(digit_sum(fast))
        

        return fast == 1