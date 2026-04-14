class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        maxlen = 1 
        tmax = 1
        charset = set()

        l = 0
        r = 1
        charset.add(s[l])
        while r < len(s):
            if s[r] not in charset:
                tmax += 1
                charset.add(s[r])
                r += 1
            else:
                tmax -= 1
                charset.remove(s[l])
                l += 1
            maxlen = max(tmax, maxlen)
        return maxlen
