class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        def dp(i, j, l1, l2, edits):
            if j >= len(word2) or i >= len(word1):
                return edits + abs(l1 - l2)    
            
            best = float('inf')
            if word1[i] == word2[j]:
                best = min(best, dp(i+1, j+1, l1, l2, edits))
            
            if word1[i] != word2[j]:
                best = min(best, dp(i, j+1, l1+1, l2, edits+1))
                best = min(best, dp(i+1, j, l1-1, l2, edits+1))
                best = min(best, dp(i+1, j+1, l1, l2, edits+1))
            
            return best
        
        return dp(0, 0, len(word1), len(word2), 0)
