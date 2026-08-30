class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # have 2 L and R pointer . move R until you get all possible letters of t in s.
        # once you get all possible values, move L to R pointer
        # add all substrings within a hashmap where characters are the keys and char length is the value
        # after the entire string has been iterated, check for min length and return that key.

        if t == "":
            return ""

        countT, window = {}, {} # create 2 hashmaps for the 

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1] , float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
        
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result, if we found a min
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                #pop from the left of our window
                window[s[l]] -= 1
                # second occurence is the multiplicity check. if after removing l pointer, 
                # the window loses a required count for the characters, then decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have-=1
                l+=1
        l,r = res
        return s[l: r+1] if resLen != float("infinity") else ""
