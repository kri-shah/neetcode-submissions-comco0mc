class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(i, path):
            if i == len(nums):
                res.add(tuple(path))
                return
            
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            backtrack(i+1, path)
        
        backtrack(0, [])
        res = [list(x) for x in res]
        
        return res