class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        # creating frequency hashmaps
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        # add the hashmap into a list
        arr = []
        for value, count in hashmap.items():
            arr.append([count,value])
        
        arr.sort() # sorts in asecning order

        # appends max values in length of k
        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])

        return res