class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        
        while i < n:
            cur_jump = nums[i]
            
            # If from this index we can directly reach or pass the end
            if i + cur_jump >= n - 1:
                return True
            
            # Find the next index that allows the farthest jump
            max_indx, max_val = i, float('-inf')
            for j in range(i + 1, min(i + cur_jump + 1, n)):
                if nums[j] + j > max_val:
                    max_val = nums[j] + j  # farthest we can reach from j
                    max_indx = j
            
            # If max_val didn’t improve, we’re stuck
            if max_indx == i:
                return False
            
            i = max_indx  # jump to the next best index
            
        return True
