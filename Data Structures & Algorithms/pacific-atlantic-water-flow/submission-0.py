class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        N = len(heights)
        M = len(heights[0])
        
        def dfs(r, c, visited):
            visited.add((r, c))
            for i, j in directions:
                newr = r + i
                newc = c + j
                if (newr >= 0 and newr < N and newc >= 0 and newc < M
                and (newr, newc) not in visited 
                and heights[newr][newc] >= heights[r][c]):
                    dfs(newr, newc, visited)

        pacific = set()
        atlantic = set()
        for c in range(M):
            dfs(0, c, pacific)
            dfs(N-1, c, atlantic)
        
        for r in range(N):
            dfs(r, 0, pacific)
            dfs(r, M-1, atlantic)

        res = []
        for r in range(N):
            for c in range(M):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res
