class Solution:
    def isAlphaNumeric(self,c):
        if 97<=ord(c)<123 or 65<=ord(c)<91 or 48<=ord(c)<=57:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        # 2 pointer solution
        l = 0
        r = len(s)-1

        # checking while the left pointer is less than right pointer
        while l<r:
            while l<r and not self.isAlphaNumeric(s[l]):
                l+=1 
            while l<r and not self.isAlphaNumeric(s[r]):
                r-=1
            
            if s[l].lower() == s[r].lower() :
                l+=1
                r-=1
            # retrn true if they are all the same characters
            else:
                return False
        return True

       