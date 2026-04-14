class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combo(i, path):
                
            if len(path) == k:
                res.append(path[:])
                return
            if i > n:
                return
            
            path.append(i)
            combo(i+1, path)
            path.pop()
            combo(i+1, path)
        
        combo(1, [])
        return res