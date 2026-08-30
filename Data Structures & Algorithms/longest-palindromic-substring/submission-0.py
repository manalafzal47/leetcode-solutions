class Solution:
    def longestPalindrome(self, s: str) -> str:
        # find the palindromes in the string
        res=[]

        for i in range(len(s)):
            #odd-palindromes
            l,r=i,i
            while l>=0 and r<len(s) and s[r]==s[l]:
                res.append(s[l:r+1])
                r+=1
                l-=1
            
            #even-palindromes
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                res.append(s[l:r+1])
                r+=1
                l-=1

        # find the longest palindome in the result array
        longest_palindrome=max(res,key=len)

        return longest_palindrome
