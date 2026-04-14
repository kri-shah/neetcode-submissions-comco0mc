class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 1
        currMin = 1

        for n in nums:            
            temp = currMax * n
            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, temp, n * currMin)
            res = max(res, currMax)
        
        return res