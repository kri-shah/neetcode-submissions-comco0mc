from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append([time[1], time[2]])
        
        cost = {k:0}
        
        q = deque()
        q.append(k)
        visited = set()
        print(graph)
        while q:
            node = q.pop()
            for neig, dist in graph[node]:
                cost[neig] = min(cost.get(neig, float('inf')), 
                cost[node]+dist)
                if neig not in visited:
                    q.append(neig)
                    visited.add(neig)
        
        print(cost)
        res = float('-inf')
        for i in range(n+1):
            res = max(res, cost.get(i, float('-inf')))
        
        return res if len(cost) == n else -1
