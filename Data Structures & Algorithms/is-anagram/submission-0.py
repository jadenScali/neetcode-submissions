class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        letters_cleared = 0

        for letter in t:
            if letter not in count:
                return False
            count[letter] -= 1

            if count[letter] == 0:
                letters_cleared += 1
            elif count[letter] < 0:
                return False
        
        return True



        