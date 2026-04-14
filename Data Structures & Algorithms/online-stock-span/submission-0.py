class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack) - 1
        res = 0
        while i > -1 and self.stack[i] <= price:
            i -= 1
            res += 1
        
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)