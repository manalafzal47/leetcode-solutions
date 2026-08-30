from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        # need to check count in s
        for char in s:            
            count_s[char] = count_s.get(char,0)+1

        # need to check count in t 
        for char in t:
            count_t[char]=count_t.get(char,0)+1

        # and check if they both match the counts of the characters
        # then return true
        # otherwise false
        return count_s == count_t
