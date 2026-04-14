class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dp(i, s):
            key = (i, s)
            
            if key in memo:
                return memo[key]
            if s == n:
                return 0
            if s > n or i * i > n:
                return float('inf')
            
            take = 1 + dp(i, s + (i * i))
            skip = dp(i + 1, s)
            
            memo[key] = min(take, skip)
            return memo[key]
        
        return dp(1, 0)
