class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dp(i, prev):
            # nums=[4,10,4,3,8,9]
            if i == len(nums):
                return 0
            
            best = dp(i+1, prev)
            if prev == -1 or nums[prev] < nums[i]:
                best = max(best, dp(i + 1, i)+1)

            return best
        
        return dp(0, -1)
            
            