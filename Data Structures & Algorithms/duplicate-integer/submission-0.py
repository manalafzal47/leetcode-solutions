class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap=set()
        # going through the iteration numbner in the array
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)

        return False

        # going through the values in the array



