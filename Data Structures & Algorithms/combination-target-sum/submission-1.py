class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, path, s):
            
            if s > target or i >= len(nums):
                return
            
            if s == target:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i, path, s+nums[i])
            path.pop()
            backtrack(i+1, path, s)
        backtrack(0, [], 0)
        return res