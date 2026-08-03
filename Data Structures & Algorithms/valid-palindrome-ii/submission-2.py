class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_Pal(l:int,r:int)->bool:
            while l<r:
                while l<r and not s[l].isalnum():
                    l+=1
                while l<r and not s[r].isalnum():
                    r -=1
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r -=1
            return True
        l,r=0 ,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return is_Pal(l+1,r) or is_Pal(l,r-1)
            l+=1
            r-=1
        return True
        