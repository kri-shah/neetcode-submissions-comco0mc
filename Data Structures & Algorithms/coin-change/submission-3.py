class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(i, s):
            key = (i, s)
            
            if key in memo:
                return memo[key]
            
            if i >= len(coins) or s > amount:
                return float('inf')
            
            if s == amount:
                return 0
            
            memo[key] = min(1 + dp(i, s + coins[i]), dp(i + 1, s))

            return memo[key]
        
        res = dp(0, 0)
        return res if res != float('inf') else -1
        