class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        def backtrack(indx):
            if sum(curr) > target or indx >= len(nums):
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return
                
            curr.append(nums[indx])
            backtrack(indx)
            
            curr.pop()
            backtrack(indx+1)
            
        
        backtrack(0)
        return res
