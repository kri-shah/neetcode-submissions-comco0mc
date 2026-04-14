from collections import defaultdict
class Solution:
    def freq_arr(self, s):
        arr = [0]*26
        for c in s:
           arr[ord(c)-ord('a')] +=1
        return tuple(arr)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[self.freq_arr(s)].append(s)
        
        res = []
        for key, val in anagrams.items():
            res.append(val)
        
        return res