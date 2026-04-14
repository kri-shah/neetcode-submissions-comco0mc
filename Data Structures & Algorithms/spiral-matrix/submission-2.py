class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])
        u = 0
        d = len(matrix)
        res = []
        while l < r and u < d:
            for i in range(l, r):
                res.append(matrix[u][i])
            u+=1
            for i in range(u, d):
                res.append(matrix[i][r - 1])
            r-=1
            if not (l < r and u < d):
                break
            for i in range(r-1, l-1, -1):
                res.append(matrix[d - 1][i])
            d-=1
            for i in range(d-1, u-1, -1):
                res.append(matrix[i][l])
            l+=1
        
        return res
