class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        df = 0
        mn = math.inf

        # for price in prices:
        #     if price < mn:
        #         mn = price
        #     elif price > mx:
        #         mx = price


        for price in prices:
            if (price - mn) > df:
                df = price - mn
            if price < mn:
                mn = price
        
        return df

        