class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        res = float('inf')
        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= target:
                res = min(res, r-l+1)
            
            while curr_sum >= target:
                curr_sum -= nums[l]
                l += 1
                if curr_sum >= target:
                    res = min(res, r-l+1)
        
        return res if res != float('inf') else 0