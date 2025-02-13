class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        # starting from left, keep track of the current minimum to check max profit for each day after it
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                output += prices[i] - prices[i - 1]
        return output
