class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # optimal approach:
        # keep a monotonic queue (and keep greater values, on the top 
        # of the queue, while removing lower values each time
        # remove all the smaller candidates from the back
        # push current index at the back
        # record answer when the first window is formed 

        res = [] # result (holds one max per window)
        q = deque() # deque of indexes 
        l = 0

        for r in range(len(nums)):
            # maintain the decreasing order in deque
            # remove indexes from the back, while current val is 
            # bigger or equal, since those removed indexes will not 
            # be future max 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # append the current index 
            q.append(r)

            # remove the top index if it outside window [l,r] 
            if q[0] < l: 
                q.popleft()
            
            # if window size reached k, record the max and slide the left boundary. window size will be (l-r+1)
            if (r - l + 1) >= k: 
                # front of deque (will be max of this window )
                res.append(nums[q[0]]) 
                # move the window by increment left boundary
                l += 1

        
        return res 

    # brute force approach:
        # loop through array by keeping sliding window = k 
        # need to loop through each val inside the sliding window 
        # of length = k and then find the max, and add that max
        # inside of the res array

        # then add the max of each sliding window inside of a new 
        # res array 
        # keep sliding window right one position until the length 
        # of it becomes greater than k 

        # time complexity: O(n*k) because loop through n each k times 
        # space complexity: O(n)

