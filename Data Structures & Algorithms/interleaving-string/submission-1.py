class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dp(i, j, k, flag):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            res = False
            if flag:
                if s1 and s1[i] != s3[k]:
                    return False
                while i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                    i += 1
                    k += 1
                
                res = dp(i, j, k, False) or res
            
            else:
                if s2 and s2[j] != s3[k]:
                    return False
                
                while j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                    j += 1
                    k += 1
                
                res = dp(i, j, k, True) or res
            
            return res
        
        return dp(0, 0, 0, True) or dp(0, 0, 0, False) 