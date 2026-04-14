import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [s*-1 for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            print(heap)
            s1 = heapq.heappop(heap) 
            s2 = heapq.heappop(heap)
            if s2 > s1:
                heapq.heappush(heap, s1 - s2)
        
        return heap[0]*-1 if heap else 0
            