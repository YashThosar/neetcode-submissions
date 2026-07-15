class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_n = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        n = len(s_n)
        l = 0
        r = n-1
        while l<r:
            if s_n[l]==s_n[r]:
                l+=1
                r-=1
            else:
                return False
        return True

        