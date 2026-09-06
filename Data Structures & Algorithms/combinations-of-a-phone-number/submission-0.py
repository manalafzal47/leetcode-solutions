class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create mapping for the digits and their possible characters


        # then traverse the digit in digits and check the possible mappings

        # the backtracking options will be:

        # 1. check if all digit from one digit has been checked and mapped to the next digit 

        combinations = {
                        "2": "abc", 
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz",
                    }

        result = []

        # create dfs function that checks the index and path 
        def dfs(index, path):
            if not digits:
                return []

            if index == len(digits):
                result.append("".join(path))
                return 
                        
            letters = combinations[digits[index]] # this gets the 

            for letter in letters:
                # check if the value in the digits has been added
               path.append(letter)

               # recurse
               dfs(index + 1, path)

               # undo
               path.pop()
            

        dfs(0, [])
        return result





                