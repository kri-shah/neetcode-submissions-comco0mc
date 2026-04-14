class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = dict()
        def dp(i, first):
            key = (i, first)
            if key in cache:
                return cache[key]
            if i >= len(nums) or (i == len(nums) - 1 and first):
                return 0
            
            cache[key] =  max(dp(i + 1, first),
                nums[i] + dp(i+2, first or i == 0))
            
            return cache[key]
        
        return max(dp(0, True), dp(1, False))
