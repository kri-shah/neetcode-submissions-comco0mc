import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            return dist

        heap = []
        for point in points:
            heapq.heappush(heap, [distance(point)*-1, point])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [x[1] for x in heap]
        return res