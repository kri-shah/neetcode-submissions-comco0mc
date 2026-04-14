class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combo(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(i, n+1):
                path.append(j)
                combo(j + 1, path)
                path.pop()
        
        combo(1, [])
        return res