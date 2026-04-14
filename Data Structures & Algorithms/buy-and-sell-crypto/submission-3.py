class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = l + 1
        profit = 0
        while r < len(prices):
            print(f"l: {l} r:{r}")
            profit = max(profit, (prices[r] - prices[l]))
            if prices[l] > prices[r]:
                l = r
            r+=1


        return profit
