class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        degree = defaultdict(int)
        q = deque()
        for i in range(n):
            degree[i] += len(graph[i])
            if degree[i] == 1:
                q.append(i)
                
        remaining = n
        while q:
            q_len = len(q)
            if remaining <= 2:
                return list(q)
            for _ in range(q_len):
                node = q.popleft()
                remaining -= 1
                for neigh in graph[node]:
                    degree[neigh] -= 1
                    if degree[neigh] == 1:
                        q.append(neigh)
        
        return [0]
