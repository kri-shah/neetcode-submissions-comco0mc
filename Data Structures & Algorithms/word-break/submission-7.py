class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        def dp(indx):        
            if indx in cache:
                return cache[indx]
            
            for w in wordDict:
                if s[indx:indx+len(w)] == w:
                    
                    if dp(indx+len(w)):
                        cache[indx] = True
                        return True
            cache[indx] = False
            return False
        
        return dp(0)