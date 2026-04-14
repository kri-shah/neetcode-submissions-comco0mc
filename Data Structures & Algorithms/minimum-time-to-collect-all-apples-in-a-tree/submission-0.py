from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(cur, par):
            time = 0
            
            for neigh in tree[cur]:
                if neigh == par:
                    continue                
                
                neigh_time = dfs(neigh, cur)
                if neigh_time > 0 or hasApple[neigh]:
                    time += neigh_time + 2
            
            return time
        

        return dfs(0, -1)
                    

                