class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        # have 3 indexes that can be checked to see if the value matches
        for i in range(len(nums)):
            # skip over any duplicates in i
            if i > 0 and nums[i] == nums[i-1]:
                continue  
            
            j = i + 1
            k = len(nums) - 1 

            while j < k:
                sum_nums = nums[i] + nums[j] + nums[k]

                if sum_nums < 0:
                    j += 1
                    
                elif sum_nums > 0:
                    k -= 1

                elif sum_nums == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1
                
                    # if there is a duplicate in j then skip over it
                    while j < k and nums[j] == nums[j-1]:
                        j += 1 

        return result 