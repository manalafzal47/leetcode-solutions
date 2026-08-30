class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set to check if it contains any duplicate
        hashset=set()

        for n in nums:
            # if index already in hashset, means it is a duplicate 
            if n in hashset:
                return True
            
            else:
                hashset.add(n)
            
        return False
