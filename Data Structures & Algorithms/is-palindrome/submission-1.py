class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = "".join([c for c in s if c.isalnum()])
        formatted = formatted.lower()
        
        l = 0
        r = len(formatted) -1
        while l <= r:
            if formatted[l] != formatted[r]:
                return False
            l += 1
            r -= 1
        
        return True