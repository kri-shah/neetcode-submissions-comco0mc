import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p)/m)
            
            if time <= h:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        
        return res