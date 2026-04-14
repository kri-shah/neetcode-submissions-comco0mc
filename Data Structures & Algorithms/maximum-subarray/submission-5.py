class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        curmax = float('-inf')
        for i in nums:
            if i > curmax and curmax < 0:
                curmax = i
            else:
                curmax += i
            maxsum = max(maxsum, curmax)
        
        return maxsum