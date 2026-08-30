class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap={}

        for num in nums:
            if num in hashmap:
                return num
            hashmap[num]=1+hashmap.get(num, 0)

        return -1