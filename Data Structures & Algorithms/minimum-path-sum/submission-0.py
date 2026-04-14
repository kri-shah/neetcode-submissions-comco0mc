class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dp = [grid[0][0]]
        for c in range(1, COLS):
            dp.append(dp[c - 1] + grid[0][c])
        
        for r in range(1, ROWS):
            curr_row = [0] * COLS
            for c in range(COLS):
                if c == 0:
                    curr_row[c] = dp[c] + grid[r][c]
                else:
                    curr_row[c] = grid[r][c] + min(curr_row[c - 1], dp[c])
            dp = curr_row[:]

        return dp[-1]
