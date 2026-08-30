class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        for i in range(len(s)):
            # checking even-length palindromes
            l=i
            r=i+1
        
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                r+=1
                l-=1

            # checking odd-length palindromes

            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                r+=1
                l-=1
            
        return res


