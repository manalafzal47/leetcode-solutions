class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # create result array
        result = []

        
        # create dfs function that includes index and path 
        def dfs(index, path):
            if index == len(nums):
                result.append(path.copy())
                return result

            path.append(nums[index])

            # check if nums will be included
            dfs(index + 1, path)

            # pop the last value to check other values
            path.pop()

            # otherwise if it will not be included 
            dfs(index + 1, path)

        dfs(0, [])
        return result 