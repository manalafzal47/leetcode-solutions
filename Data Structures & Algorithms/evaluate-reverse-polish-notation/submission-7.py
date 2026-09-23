class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # first determine if you get any of the operators, 
        # then you need to do that certain arithmetic on the previous 
        # values inside the stack
        stack = []
        operators = ["+", "-", "*", "/"]
        res = 0

        for t in tokens:
            # if t not an operator then push onto stack
            if t not in operators:
                stack.append(int(t))

            # if t is a 
            if stack and t in operators:
            # if the current value is in the stack, 
            # then need to push the last values on the stack
                rVal = stack.pop()
                lVal = stack.pop()

                # perform these arithmetics on it 
                if t == "+":   
                    # where to get the last values from stack ?
                    res = lVal + rVal
                    stack.append(res)
                
                elif t == "*":
                    res = lVal * rVal
                    stack.append(res)

                elif t == "-":
                    res = lVal - rVal
                    stack.append(res)

                elif t == "/":
                    res = int(lVal / rVal)
                    stack.append(res)


        # then return the last value 
        return stack[-1]
