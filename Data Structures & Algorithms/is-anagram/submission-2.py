class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        
        for char in s:
            if char in counter:
                char_count = counter[char]
                char_count += 1
                counter[char] = char_count
            else:
                counter[char] = 1
        
        for char in t:
            if char not in counter:
                return False
            else:
                char_count = counter[char]
                char_count -= 1
                counter[char] = char_count

        for key, value in counter.items():
            if value != 0:
                return False
        
        return True