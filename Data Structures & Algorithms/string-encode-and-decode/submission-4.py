class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "$" + word
        return res
    
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i 
            while s[j] != "$":
                j += 1
            chars = int(s[i:j])
            i = j + 1
            j = i + chars
            res.append(s[i:j])
            i = j
        
        return res