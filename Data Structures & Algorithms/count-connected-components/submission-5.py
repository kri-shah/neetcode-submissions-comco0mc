class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            
            if root1 == root2:
                return 0
            
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1] += rank[root2]
            else:
                par[root1] = root2
                rank[root2] += rank[root1]
            
            return 1
        
        res = n
        
        for u, v in edges:
            res -= union(u, v)
        
        return res
            
            