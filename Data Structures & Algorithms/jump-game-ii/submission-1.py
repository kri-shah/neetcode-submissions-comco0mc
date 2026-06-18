class Solution:
    def jump(self, nums: List[int]) -> int:
        res = nxt = curr = 0
        
        for i in range(len(nums)):
            nxt = max(nxt, nums[i] + i)
            if curr >= len(nums) - 1:
                return res
            if curr == i:
                curr = nxt
                res += 1
        
        return res