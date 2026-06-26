class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        n = len(s)
        l, r = 0, 1
        longest = 0
        while l < n:

            if r >= n:
                break
            
            freq = {} # letter : freq
            for i in range(l,r+1):
                curr = s[i]
                if curr not in freq:
                    freq[curr] = 1
                else:
                    freq[curr] += 1
            
            biggest_freq = max(freq.values())
            window_size = r - l + 1
            if window_size - biggest_freq <= k:
                r += 1
                longest = max(longest, window_size)
            else:
                l += 1
        
        return longest

                
