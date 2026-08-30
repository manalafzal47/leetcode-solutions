class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # turns heap into min-heap
        # if heap has more than k elements, keep removing the smallest ones
        while len(self.minHeap)>k:  # fix the stream of admissions
            heapq.heappop(self.minHeap)

    # adds new number and updates heap accordingly
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)