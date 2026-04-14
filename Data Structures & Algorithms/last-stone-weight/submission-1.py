import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [s*-1 for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            print(heap)
            s1 = heapq.heappop(heap) * -1
            s2 = heapq.heappop(heap) * -1
            if s1 > s2:
                heapq.heappush(heap, (s1-s2)*-1)
        
        return heap[0]*-1 if heap else 0
            