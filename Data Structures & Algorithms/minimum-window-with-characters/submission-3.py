class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}

        for l in t:
            target[l] = target.get(l, 0) + 1
        
        keys_goal = len(target.keys())
        keys_met = 0
        freq = {}
        n = len(s)
        i = 0
        shortest = (None, None)

        for j in range(n):
            l = s[j]
            if l in target:
                freq[l] = freq.get(l, 0) + 1

                if freq[l] == target[l]:
                    keys_met += 1
            
            while keys_met == keys_goal:
                if shortest == (None, None) or abs(i-j) < abs(shortest[0] - shortest[1]):
                    shortest = (i, j)
                    
                l = s[i]
                if l in target:
                    freq[l] -= 1

                    if freq[l] < target[l]:
                        keys_met -= 1
                
                i += 1
        
        if shortest == (None, None):
            return ""
        
        return s[shortest[0]:shortest[1]+1]

                    





            
            

            

        
