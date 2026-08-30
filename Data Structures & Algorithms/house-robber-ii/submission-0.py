class Solution:
    def rob(self, nums: List[int]) -> int:
        #base case if only 1 element in array
        if len(nums)==1:
            return nums[0]

        def house_robber(nums_arr):
            prev1,prev2=0,0
            for n in nums_arr:
                temp1=max(prev1, prev2+n)
                prev2=prev1
                prev1=temp1

            return prev1
        
        return max(house_robber(nums[1:]), house_robber(nums[:-1])) # this is 

