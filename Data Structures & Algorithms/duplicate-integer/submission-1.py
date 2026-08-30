class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}

        for i in range(len(nums)):
            # adding the values of the hashmap
            hashmap[nums[i]]=hashmap.get(nums[i], 0)+1
             
            if hashmap[nums[i]]>1:
                return True
        
        return False

