class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if open < n
        # only add a closing parenthesis if closed < n
        # valid IIF open == closed == n

        stack=[]
        res=[]
        
        def backtrack(openN, closedN):
            # edge case when open and closed are both equal to n
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            # case 1: add open parentheses if openCount is less than n
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            
            # case 2: add closed parenthesis if closedCount is less openCount
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        
        backtrack(0,0)
    
        return res
    
            
