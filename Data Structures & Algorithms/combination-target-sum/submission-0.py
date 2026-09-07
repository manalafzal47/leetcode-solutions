class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # create dfs function that check index, path, sum 
        def dfs(index, path, value):

            if value == target:
                result.append(path.copy())
                return result  
            
            if index == len(nums) or value > target:
                return 

            # append
            path.append(nums[index])

            # value is being added 
            dfs(index, path, value + nums[index])

            # undo
            path.pop()

            # value not being added  
            dfs(index + 1, path, value)

        dfs(0, [], 0)
        return result