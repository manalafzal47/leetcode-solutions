class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort array in order to find duplicates
        candidates.sort()

        # create result 
        result = []
        i = 0

        # create dfs with index, path, value
        def dfs(i, path, value):
            # return if value > target or i == len(Candidates) 
            # then return empty
            if value > target:
                return 

            # if value == target then return the result
            if value == target:
                result.append(path.copy())
                return 

            # can't use duplicates - so first sort the array, and then 
            # check if the last value is not the same as the current 
            # value then onyl append
            for j in range(i, len(candidates)):
                # if there is a duplicate then skip over it
                if j > i and candidates[j] == candidates[j-1]:
                    continue 

                # append the current value to result 
                path.append(candidates[j])

                # backtrack - add the current value with the current 
                # index to match the target
                dfs(j + 1,  path, value + candidates[j])

                # pop
                path.pop()

        dfs(0, [], 0)
        return result 




         