class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [1,3,4,0,4]
        1. 'claim' this as our stock to hold + sell curr stock
        2. do nothing move on 
        base case 
        if i == len(prices): return 0 
        max(dp(i+1, s),  prices[i] - prices[s] + dp(i+1, i), dp(i+1, -1)
        """
        def dp(i, can_buy):
            if i >= len(prices):
                return 0
            best = dp(i+1, can_buy)
            if can_buy:
                best = max(best, dp(i+1, False) - prices[i])
            else:
                best = max(best, dp(i+2, True) + prices[i])
            
            return best
        
        return dp(0, True)