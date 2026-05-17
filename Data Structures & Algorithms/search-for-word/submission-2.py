class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (i, j) in visited or i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != word[k]:
                return False
            if board[i][j] == word[k]:
                visited.add((i, j))
                if (dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) 
                or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)):
                    return True
                visited.remove((i, j))
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        
        return False
        
