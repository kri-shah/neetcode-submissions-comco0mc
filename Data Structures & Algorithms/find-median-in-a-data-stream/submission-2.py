# keep 2 heapsd
#smaller -> max heap
#larger -> min heap
# maintain 2 invarients:
#   1. max element in smaller <= min element in larger
#   2. len(smaller) ~= len(larger)

# [1,2, 3],    [4, 5, 100]

class MedianFinder:

    def __init__(self):
        self.smaller = [] # max heap
        self.larger = [] # min heap

    def addNum(self, num: int) -> None:
        if self.larger and num <= self.larger[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.larger, num)
        
        if abs(len(self.larger) - len(self.smaller)) >= 2:
            if len(self.smaller) > len(self.larger):
                val = -heapq.heappop(self.smaller)
                heapq.heappush(self.larger, val)
            else:
                val = heapq.heappop(self.larger)
                heapq.heappush(self.smaller, -val)


    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        elif len(self.smaller) < len(self.larger):
            return self.larger[0]
        else:
            return (-self.smaller[0] + self.larger[0]) / 2

