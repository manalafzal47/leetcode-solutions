class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p,s in zip(position, speed)]  # creating tuple of (position,speed)
        
    # Intuition: if time of position it takes to get to target is less than one on right, then that means it must collide. since we are going in reverse order.

    # calculate the time array
        for p,s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target-p)/s) # calculate time it takes
# check the greater position with the lower one to check if they collide. and check if stack is more than 2 because that means we are at the end of the comparisons 
            if len(stack)>=2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)
