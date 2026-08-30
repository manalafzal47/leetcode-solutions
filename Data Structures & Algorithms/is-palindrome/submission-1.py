class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (s := re.sub(r"[^A-Za-z0-9]", "", s).lower()) == s[::-1]