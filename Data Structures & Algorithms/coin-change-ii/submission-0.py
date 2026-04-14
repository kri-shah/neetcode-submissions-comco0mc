class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dp(i, s):
            key = (i, s)
            if key in cache:
                return cache[key]
            
            if s == amount:
                return 1
            if i >= len(coins) or s > amount:
                return 0
            
            res = dp(i, s + coins[i]) + dp(i+1, s)
            cache[key] = res
            
            return cache[key]
        
        return dp(0, 0)