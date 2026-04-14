class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        visited = dict()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, prev):
            
            
            if not (r >= 0 and r < ROWS
                and c >= 0 and c < COLS and matrix[r][c] > prev):
                return 0
            if (r, c) in visited:
                return visited[(r, c)]
            res = 0
            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                res = max(res, 1 + dfs(newr, newc, matrix[r][c]))
            
            visited[(r, c)] = res
            return visited[(r, c)]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float('-inf')))
        
        return res
        
        