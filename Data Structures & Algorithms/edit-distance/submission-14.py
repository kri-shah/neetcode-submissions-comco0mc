class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        memo = dict()
        def dp(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]

            if i == len(word1):
                return len(word2) - j 
            if j == len(word2):
                return len(word1) - i
            
            best = float('inf')
            if word1[i] == word2[j]:
                best = dp(i+1, j+1)
            
            if word1[i] != word2[j]:
                best = min(best, dp(i, j+1) + 1)
                best = min(best, dp(i+1, j) + 1, dp(i+1, j+1,) + 1)
            memo[key] = best

            return memo[key]
        
        return dp(0, 0)
