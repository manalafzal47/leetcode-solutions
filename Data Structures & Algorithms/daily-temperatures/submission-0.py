class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # initialize stack
        stack = []
        answer=len(temperatures)*[0]
    
# traverse all the values in temperature. store the indexes

        for i in range(len(temperatures)):
        # if the value at the current stack is greater than 
        # the last value in the stack, then pop the last value 
        # --> meaning warmer temperature has been found
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index=stack.pop()
                answer[prev_index]=i-prev_index  # calculate the # of days of waiting for next warm temp

        # otherwise, if the value at current stack is less than the last value, then basically keep that value and add the next value after that into the stack. --> keep going until you find the next warmer tempp. also need to keep track of all the indexes you have checked.
  
            stack.append(i)
    
    # at the end of the loop, any remaining indexes,will have no warmer days so they will be 0.  --> because we initialized the answer array as arrays of 0 it works.

        return answer 
