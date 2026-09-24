class Solution:
    def isValidAlphaNumeric(self, c:str)->bool:
        # return true/false if its valid letters and numbers
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

    def isPalindrome(self, s: str) -> bool:
        # check l and r pointer and check if its not a alphanumeric then skip over it
        l, r = 0, len(s) - 1

        # then check if the s[l] == s[r] to see if its a valid palindrome or not
        while l < r:
            while l < r and not self.isValidAlphaNumeric(s[l]):
                l += 1
            
            while r > l and not self.isValidAlphaNumeric(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1 
            r -= 1 

        return True  


