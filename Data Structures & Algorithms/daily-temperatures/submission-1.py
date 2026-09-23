class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # check if the curr temp is greater than the max value found so far, and 
        # then increment count of warmer temp
        res = len(temperatures) * [0]
        stack = []

        for i in range(len(temperatures)):
            # if the stack is valid and the current value is less than the
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_index = stack.pop() # pop last index in stack
                res[pre_index] = i - pre_index  # find the difference between warmer temp and last computed index 
                    
            stack.append(i) # adding value to stack if its not a greater temp found 

        return res 
