class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        # find the count of each element in the array
        for n in nums:
            if n not in hashmap:
                hashmap[n]=1
            else:
                hashmap[n]+=1

        result = []

        # sort the key and values now
        for index, count in hashmap.items():
            result.append([count,index])
        
        result.sort(reverse=True) # sorting by count 
        print(result)
            
        output=[]

        for i in range(k):
            output.append(result[i][1])

        # return upto k
        return output
      