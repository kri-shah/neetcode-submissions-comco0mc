class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)
        
        def is_valid(sub_str):
            return sub_str == sub_str[::-1]

        def backtrack(i, curr_str):
            if i == n:
                l = ["".join(p) for p in path]
                t = 0
                for k in l:
                    t += len(k) 
                if t == n:
                    res.append(l)
                return 
                
            curr_str.append(s[i])
            if is_valid(curr_str):
                path.append(curr_str)
                backtrack(i + 1, [])
                path.pop()
            backtrack(i + 1, curr_str)

            
        backtrack(0, [])
        return res