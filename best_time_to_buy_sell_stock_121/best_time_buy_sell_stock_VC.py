class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = max(prices)
        Min = min(prices)
        if (index(Min) == len(prices)-1):
            return 0
        while index(Max) > index(Min):
            prices.remove(Max)
            Max = max(prices)
        return Max - Min