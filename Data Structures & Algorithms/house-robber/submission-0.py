class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0

        for i in range(len(nums)):
            #skipping the current element or taking the element of 2 houses down and adding the current element
            temp=max(rob1, rob2+nums[i])
            rob2=rob1
            rob1=temp
        
        return rob1