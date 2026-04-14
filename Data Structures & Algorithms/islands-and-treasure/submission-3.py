from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31-1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(q):
            while q:
                x, y = q.popleft()
                for i, j in directions:
                    newr, newc = x + i, y + j
                    if (newr >= 0 and newr < ROWS 
                    and newc >= 0 and newc < COLS):
                        if grid[newr][newc] == inf:
                            grid[newr][newc] = grid[x][y] + 1
                            q.append([newr, newc])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        bfs(q)

