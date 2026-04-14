class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            return climb(step + 1) + climb(step + 2)
        
        return (climb(1) + climb(2))