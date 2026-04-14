class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(curr_nums, used):
            if len(curr_nums) == len(nums):
                res.add(tuple(curr_nums))
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                curr_nums.append(nums[i])
                backtrack(curr_nums, used)
                used.remove(i)
                curr_nums.pop()
        
        backtrack([], set())
        return [list(tup) for tup in res]
