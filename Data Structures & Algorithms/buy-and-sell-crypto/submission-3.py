class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxProfit=0
        profit=0

        while j < len(prices):
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                maxProfit=max(maxProfit,profit)
            else:
                i=j
            j+=1
        return maxProfit

