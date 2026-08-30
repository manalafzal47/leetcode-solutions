class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # create the stack 
        maxArea = 0
        stack = []

        # while the stack is valid and the last value height is greater than current height, this means that the next value is greater thjan the current value, meaning it must be popped, while stack and stack[-1][1] > h:
        for i, h in enumerate(heights):
            # make current start equal to i
            start = i

            while stack and stack[-1][1] > h:
                # pop the current indices from stack: index,height = stack.pop()
                index, height = stack.pop()
                # compute the maxArea to be max(maxArea, height*(i-index)) which means width is the current index - last computed index
                maxArea = max(maxArea, height*(i-index))
                # make start equal to the last computed index --> start = index
                start = index
            # otherwise append the start, index to the stack
            stack.append((start,h))

        # since stack is (i, h), can just go through to find max area
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))

        return maxArea
        # max Area will be calculated using this formula: while the stack is not empty 
        # maxArea max(maxArea, height * ( len(heights)-i))

