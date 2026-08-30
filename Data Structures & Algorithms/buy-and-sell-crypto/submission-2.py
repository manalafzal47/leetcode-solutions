class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxProfit=0
        profit=0

        lowest=prices[0] #initializing to the first element

        for price in prices:
            if lowest>price:
                lowest=price
            maxProfit=max(maxProfit,price-lowest)

        return maxProfit

