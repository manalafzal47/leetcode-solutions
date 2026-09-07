class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # permutation cannot have duplicate - so need to use set to find the possible subsets
        permutation_set = set()

        # create dfs function that includes index and path 
        def dfs(index, path):
            if index == len(nums):
                result.append(path.copy())
                return result 

            for n in nums:
                # if value not already in set - add to subset 
                if n not in permutation_set:
                    path.append(n)
                    permutation_set.add(n)

                    # move the path up
                    dfs(index + 1, path)

                    # undo backtracking
                    path.pop()
                    permutation_set.remove(n)

        dfs(0, [])
        return result 