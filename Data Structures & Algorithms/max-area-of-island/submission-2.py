class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for arr in grid:
            print(arr)
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(pos):
            stack = [pos]
            visited.add(tuple(pos))
            area = 1
            while stack:
                r, c = stack.pop()
                for i, j in directions:
                    newr, newc = r + i, c + j
                    if (newr >= 0 and newc >=0
                        and newr < ROWS and newc < COLS):
                        if grid[newr][newc] == 1 and (newr, newc) not in visited:
                            area += 1
                            stack.append([newr, newc])
                            visited.add((newr, newc))
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(dfs([r, c]), max_area)
        
        return max_area
                
