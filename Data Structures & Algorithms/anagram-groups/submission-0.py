class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create hashmap { strs element, list of elements }
        # check if strs element is in hashmap -> if yes (meaning the characters are the same ?  
        # if no? then add to hashmap as the key 

        # sort the words in the strs array to check if its matching the words.

        # return hashmap values

        hashmap = {}

        for word in strs:
            # store the alphaticized word 
            key = ''.join(sorted(word)) 

            # if key not in hashmap, means that we create a list to store the anagrams 
            if key not in hashmap:
                hashmap[key] = []

            # if key exists . then add to the anagrams list for that word
            hashmap[key].append(word)

        res=[]
        for val in hashmap.values():
            res.append(val)

        return res

            

                                                                                       
   
            
    