class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        cache = dict()
        def backtrack(s):
            if s in cache:
                return cache[s]
            if s == target:
                return 1
        
            res = 0
            for i in range(len(nums)):
                if s > target:
                    break
                res += backtrack(s+nums[i])
            cache[s] = res
            
            return cache[s]

        
        return backtrack(0)