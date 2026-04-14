from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31-1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(pos):
            q = deque()
            q.append(pos)
            visited = set()
            while q:
                x, y = q.popleft()
                for i, j in directions:
                    newr, newc = x + i, y + j
                    if (newr >= 0 and newr < ROWS 
                    and newc >= 0 and newc < COLS):
                        print(grid[newr][newc])
                        if grid[newr][newc] != -1:
                            grid[newr][newc] = min(grid[newr][newc], grid[x][y] + 1)
                            if (newr, newc) not in visited:
                                q.append([newr, newc])
                                visited.add((newr, newc))
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs([r, c])


