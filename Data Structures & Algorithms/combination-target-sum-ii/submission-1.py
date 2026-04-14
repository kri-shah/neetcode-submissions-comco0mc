class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def backtrack(i, s, path):
            if s == target:
                res.add(tuple(path))
                return
            if s > target or i >= len(candidates):
                return
            
            backtrack(i+1, s, path)
            path.append(candidates[i])
            backtrack(i+1, s+candidates[i], path)
            path.pop()
        
        backtrack(0, 0, [])
        res = list(list(arr) for arr in res)
        return res