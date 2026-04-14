class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= self.max_heap[0]:
            heapq.heappush(self.min_heap, num * -1)
        else:
            heapq.heappush(self.max_heap, num)
        
        if abs(len(self.min_heap) - len(self.max_heap)) >= 2:
            if len(self.min_heap) > len(self.max_heap):
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, val * -1)
            else:
                val = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val * -1)

    def findMedian(self) -> float:
        
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]
        else:
            return (-self.min_heap[0] + self.max_heap[0]) / 2
        