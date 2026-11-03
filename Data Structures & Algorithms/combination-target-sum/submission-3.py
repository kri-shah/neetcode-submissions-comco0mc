class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def combo(i, s):
            if i >= len(nums) or s > target:
                return
            
            if target == s:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                combo(j, s + nums[j])
                path.pop()
        
        combo(0, 0)
        return res