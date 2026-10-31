class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            curr = [1] * n
            for c in range(1, n):
                curr[c] = dp[c] + curr[c - 1]
            dp = curr[:]
        
        return dp[-1]
        