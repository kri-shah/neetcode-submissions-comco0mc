import heapq
class MedianFinder:
    def __init__(self):
        self.small_heap = [] #small heap / max heap
        self.large_heap = [] #large heap / min heap
        #all values in self.small_heap <= self.large_heap

    def addNum(self, num: int) -> None:
        if self.large_heap and num > self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, num*-1)

        if len(self.small_heap) - len(self.large_heap) > 1:
            val = heapq.heappop(self.small_heap)*-1
            heapq.heappush(self.large_heap, val)
        
        if len(self.large_heap) - len(self.small_heap) > 1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, val*-1)


    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (self.small_heap[0]*-1+self.large_heap[0])/2
        elif len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0]*-1
        else:
            return self.large_heap[0]




        