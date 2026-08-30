class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1:1 , 2:1, 3:2 

        hashset=set()

        for num in nums:
            if num in hashset:
                # duplicate
                return True
            
            hashset.add(num)

        return False