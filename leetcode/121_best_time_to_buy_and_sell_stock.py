class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProf = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                highestProf = max(highestProf, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return highestProf

# solution 2:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for price in prices:
            if price < minimum:
                minimum = price
            max_profit = max(max_profit, price - minimum)
        
        return max_profit
