import heapq
from collections import deque 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0]*26
        for c in tasks:
            freqs[ord(c) - ord('A')] += 1
        
        heap = [i*-1 for i in freqs if i != 0]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task != 0:
                    q.append([task, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        
        return time