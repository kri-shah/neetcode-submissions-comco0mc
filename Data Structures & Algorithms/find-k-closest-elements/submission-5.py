
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        l = 0
        r = n - 1
        while l < r:
            m = (l+r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m
        
        l, r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            elif abs(x - arr[l]) <= abs(x - arr[r]):
                l -= 1
            else:
                r += 1
        return arr[l + 1:r]
        