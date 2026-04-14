from collections import defaultdict
class Solution:
    def freq(self, s):
        freq_dict = defaultdict(int)
        for c in s:
            freq_dict[c] += 1
        
        return freq_dict

    def isAnagram(self, s: str, t: str) -> bool:
        return self.freq(s) == self.freq(t)
        
