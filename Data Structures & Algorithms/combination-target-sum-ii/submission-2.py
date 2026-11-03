class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        path = []
        def backtrack(i, s):
            if s == target:
                res.append(path[:])
                return
            if i >= n or s > target:
                return
            
            

            path.append(candidates[i])
            backtrack(i + 1, s + candidates[i])
            path.pop()
            
            j = i 
            while j + 1 < n and candidates[j] == candidates[j + 1]:
                j += 1
            
            backtrack(j + 1, s)
        
        backtrack(0, 0)
        return res