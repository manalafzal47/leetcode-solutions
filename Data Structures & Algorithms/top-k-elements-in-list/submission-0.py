class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        arr=[]
        res=[]

        for num in nums:
            hashmap[num]=1+hashmap.get(num, 0) #getting count of every element

        for num, value in hashmap.items():
            arr.append([value, num])

        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
    
        return res

        