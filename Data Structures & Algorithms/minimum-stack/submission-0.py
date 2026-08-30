class MinStack:

    def __init__(self):
        ##NOTE: needs self because its not initialized

        # holds values from stack
        self.stack = []
    
        # holds min values from min_stack
        self.min_stack = []

    def push(self, val: int) -> None:
        # push val into stack.
        self.stack.append(val)

 
        # for pushing val into min_stack

        # if 

        # checks if val is < than latest value in min_stack.
        # if yes--> replace val on min_stack with that current val.
        # if no --> then continue


        if len(self.stack)==1:
            self.min_stack.append(val)

        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        # pop from both normal stack and min_stack
        self.stack.pop()
        self.min_stack.pop()
         
    def top(self) -> int:
        # this will be popping the latest val in stack
        return self.stack[-1]

    def getMin(self) -> int:
        # gets the latest val in min_stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()