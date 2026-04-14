class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, s, path):
            if s == target:
                res.append(path[:])
                return 0
            
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return
                
                path.append(nums[j])
                backtrack(j, s + nums[j], path)
                path.pop()
        
        backtrack(0, 0, [])
        
        return res