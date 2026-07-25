class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or word[k] != board[i][j] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            if dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1):
                return True
            
            visited.remove((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        
        return False