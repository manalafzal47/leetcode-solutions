class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array 
        
        # create result
        result = []

        # create dfs function with index, pathd
        def dfs(i, path):
            result.append(path.copy())

            # check for duplicates - skip if so
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                # add the current number to the path
                path.append(nums[j])

                # then backtrack
                dfs(j + 1, path)

                # pop
                path.pop()
            
        dfs(0, [])
        return result 

