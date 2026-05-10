class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = 0
        l = len(s) - 1

        while f < l:
            if not ('0' <= s[f] <= '9' or 'a' <= s[f] <= 'z'):
                f += 1
                continue

            if not ('0' <= s[l] <= '9' or 'a' <= s[l] <= 'z'):
                l -= 1
                continue
            
            if s[f] != s[l]:
                return False
            
            f += 1
            l -= 1

        return True

        