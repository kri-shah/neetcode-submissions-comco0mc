class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r, c):
            if (r >= n or r < 0 or c >= m or c < 0):
                return 0
            if r == n-1 and c == m-1:
                return 1 
            
            res = dp(r, c+1) + dp(r+1, c)
            
            return res
        return dp(0, 0)