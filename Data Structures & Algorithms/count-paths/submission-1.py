class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dp(r, c):
            if (r >= n or c >= m):
                return 0
            if r == n-1 and c == m-1:
                return 1 
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = dp(r, c+1) + dp(r+1, c)
            cache[(r, c)] = res
            
            return res
        return dp(0, 0)