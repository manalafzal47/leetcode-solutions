class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWidth=0
        r = len(heights)-1
        l=0

        while(l<r):
            maxWidth=max(maxWidth, min(heights[l], heights[r])*(r-l))
            if heights[r]<=heights[l]:
                r-=1
            elif(heights[l]<heights[r]):
                l+=1

        return maxWidth