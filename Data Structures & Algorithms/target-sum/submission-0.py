class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, s):
            key = (i, s)
            if key in memo:
                return memo[key]
            
            if s == target and i == len(nums):
                return 1
            
            if i >= len(nums):
                return 0
            
            res = dp(i + 1, s + nums[i]) + dp(i+1, s - nums[i])
            memo[key] = res
            
            return memo[key]
        
        return dp(0, 0)