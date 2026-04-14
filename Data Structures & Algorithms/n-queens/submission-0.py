class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        
        col_set = set()
        pos_diag = set()
        neg_diag = set()
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            
            for c in range(n):
                if (c not in col_set and (r + c) not in pos_diag 
                and (r - c) not in neg_diag):
                    pos_diag.add(r+c)
                    col_set.add(c)
                    neg_diag.add(r-c)
                    grid[r][c] = 'Q'
                    backtrack(r + 1)
                    grid[r][c] = '.'
                    col_set.remove(c)
                    pos_diag.remove(r+c)
                    neg_diag.remove(r-c)
        
        backtrack(0)
        return res
    

