class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, s1, s2):
            if i == len(nums):
                return s1 == s2
            
            return dp(i + 1, s1 + nums[i], s2) or dp(i+1, s1, s2 + nums[i])
        
        return dp(0, 0, 0)