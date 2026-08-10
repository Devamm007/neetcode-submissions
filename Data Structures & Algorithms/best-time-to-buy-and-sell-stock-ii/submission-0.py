class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_bought = False
        n = len(prices)
        profit, i = 0, 0
        while i < n:
            if stock_bought:
                profit += prices[i] - prices[i-1]
                stock_bought = False
            if i+1 == n:
                break
            if prices[i+1] < prices[i]:
                stock_bought = False
                i+=1
            elif prices[i+1] == prices[i]:
                stock_bought = False
                i+=1
            else:
                stock_bought = True
                i+=1
        return profit