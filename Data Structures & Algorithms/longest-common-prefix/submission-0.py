class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = min(len(s) for s in strs)
        res = ""

        for i in range(length):
            for j, s in enumerate(strs):
                if j == 0:
                    res += s[i]
                else:
                    if s[i] != res[i]:
                        res = res[0:-1]
                        return res
        
        return res