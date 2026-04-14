class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        num1s = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num1s += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        
        while q and num1s:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i, j in directions:
                    newr = r + i 
                    newc = c + j
                    if (newr >= 0 and newc >= 0 
                    and newr < ROWS and newc < COLS):
                        if grid[newr][newc] == 1:
                            grid[newr][newc] = 2
                            q.append([newr, newc])
                            num1s -= 1
                
            res +=1
        
        return res if num1s == 0 else -1
