from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        cycle, visit = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for neigh in graph[crs]:
                if not dfs(neigh):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True