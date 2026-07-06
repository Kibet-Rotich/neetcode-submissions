class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = "".join(char for char in s if char.isalnum())
        h,l = len(s)-1,0

        while l<=h:
            if s[l] != s[h]:
                return False
            l += 1
            h-=1
        
        return True
        