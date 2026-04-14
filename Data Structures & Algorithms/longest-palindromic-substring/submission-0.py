class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            l = i-1
            r = i + 1
            odd = [s[i]]
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    odd.insert(0, s[l])
                    odd.append(s[r])
                else:
                    break
                l -=1
                r +=1
            l = i
            r = i + 1
            even = []
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    even.insert(0, s[l])
                    even.append(s[r])
                else:
                    break
                l -=1
                r +=1
            
            if len(odd) > len(even) and len(odd) > len(res):
                res = odd
            elif len(even) > len(res):
                res = even
        
        return "".join(res)
        
        