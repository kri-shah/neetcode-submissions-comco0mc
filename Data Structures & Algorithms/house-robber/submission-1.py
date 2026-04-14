class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dp(indx):
            if indx >= len(nums):
                return 0
                
            if cache[indx] != -1:
                return cache[indx]
            
            cache[indx] = max(dp(indx+1), dp(indx+2)+nums[indx])
            
            return cache[indx]
            
        return dp(0)
