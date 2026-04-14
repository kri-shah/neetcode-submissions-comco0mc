class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = dict()
        max_freq = float('-inf')
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(max_freq, freq[s[r]])
            
            while max_freq + k <= (r - l):
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res