class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = 0
        r = n-1
        
        while l < r:
            for i in range(r - l):
                u = l
                d = r
                tr = matrix[u][l+i]
                tl = matrix[u+i][r]
                br = matrix[d][r-i]
                bl = matrix[d-i][l]
                
                matrix[u+i][r] = tr
                matrix[d][r-i] = tl
                matrix[d-i][l] = br
                matrix[u][l+i] = bl
            
            l += 1
            r -=1

