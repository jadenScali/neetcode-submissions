class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for l in s1:
            s1_freq[l] = s1_freq.get(l, 0) + 1
        
        i = 0
        n = len(s1)
        m = len(s2)
        while i + n - 1 < m:
            winodw_freq = {}
            for i in range(i, i + n):
                l = s2[i]
                winodw_freq[l] = winodw_freq.get(l, 0) + 1
            
            if winodw_freq == s1_freq:
                return True
        
        return False





        