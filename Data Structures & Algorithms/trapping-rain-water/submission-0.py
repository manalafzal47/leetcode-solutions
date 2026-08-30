class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        # keep store of the left and right max, and initialize
        l,r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res=0

        # continue checking if L<R
        while l < r:
            # check if maxLeft 
            if maxLeft < maxRight:
                l+=1
                maxLeft=max(maxLeft, height[l])
                res+=maxLeft-height[l]
            
            else:
                r-=1
                maxRight=max(maxRight, height[r])
                res+=maxRight-height[r]
        
        return res


