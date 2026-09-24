class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # since its already sorted, we check the sum of the consecutive 
    # values and then from there, we can move up the left pointer 
    # if the value of sum < target or otherwise decrement right 
    # pointer if value of sum > target 

        l, r = 0, len(numbers) - 1

        while l < r:
            sum_num = numbers[l] + numbers[r]

            if sum_num < target:
                l += 1 

            elif sum_num > target:
                r -= 1
            
            elif sum_num == target:
                return [l + 1, r + 1]

        l += 1 
        r -= 1