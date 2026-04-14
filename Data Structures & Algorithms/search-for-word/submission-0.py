class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])
        path = set()
        
        def dfs(r, c, indx):
            if indx == len(word):
                return True
            
            if (r < 0 or r >= N or c < 0 or c >= M 
            or (r, c) in path or board[r][c] != word[indx]):
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, indx+1) or dfs(r-1, c, indx+1)
            or dfs(r, c+1, indx+1) or dfs(r, c-1, indx+1))
            path.remove((r, c))
            
            return res
        
        for r in range(N):
            for c in range(M):
                if dfs(r, c, 0):
                    return True
        
        return False

