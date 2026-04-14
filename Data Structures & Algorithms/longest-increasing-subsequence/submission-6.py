class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dp(i, prev):
            key = (i, prev)
            if i == len(nums):
                return 0
            if key in cache:
                return cache[key]
            
            best = dp(i+1, prev)
            if prev == -1 or nums[prev] < nums[i]:
                best = max(best, dp(i + 1, i)+1)

            cache[key] = best
            return best
        
        return dp(0, -1)
            
            