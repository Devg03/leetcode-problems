class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            elif ((prices[i]-buyPrice) > profit):
                    profit = prices[i] - buyPrice

        return profit
