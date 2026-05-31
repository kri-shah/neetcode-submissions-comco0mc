class Solution:
    def integerBreak(self, n: int) -> int:
        res = float('inf')
        memo = {1:1}
        
        def dp(num):
            if num in memo:
                return memo[num]
            
            memo[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp(i) * dp(num - i)
                memo[num] = max(memo[num], val)
            return memo[num]
        return dp(n)
