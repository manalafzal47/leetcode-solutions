class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        l=0

        while l<r:
            element_sum=numbers[l]+numbers[r]

            if element_sum<target:
                l+=1
            elif element_sum>target:
                r-=1
            else:
                return [l+1,r+1]
        
        return []
            