class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i, n in enumerate(nums):
            diff_sum = target-n
            if diff_sum in hashmap:
                return [hashmap[diff_sum],i]
            
            hashmap[n]=i

