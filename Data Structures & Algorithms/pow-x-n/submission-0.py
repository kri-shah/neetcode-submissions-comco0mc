class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        

        def recur(num, power):
            if power == 0:
                return 1
            
            res = recur(num * num, power // 2)
            
            return num * res if power % 2 else res
        
        res = recur(x, abs(n))
        return res if n > 0 else 1/res
