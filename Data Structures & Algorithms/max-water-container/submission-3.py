class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return max area using difference between (l-r) * min(heights[l] - heights[r])

        l, r = 0, len(heights) - 1 
        maxArea = 0
        area = 0

        while l < r:
            area = min(heights[l], heights[r])*(r-l)

            if heights[l] <= heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1 
        
            maxArea = max(maxArea, area)
        
        return maxArea
            