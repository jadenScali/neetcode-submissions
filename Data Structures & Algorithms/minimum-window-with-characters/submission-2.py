class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for l in t:
            freq_t[l] = freq_t.get(l, 0) + 1

        freq_s = {}
        for l in s:
            freq_s[l] = freq_s.get(l, 0) + 1
            freq_t[l] = freq_t.get(l, 0)

        for key in freq_t:
            if freq_s.get(key, 0) < freq_t[key]:
                return ""

        i, j = 0, len(s) - 1
        while freq_t[s[i]] < freq_s[s[i]]:
            freq_s[s[i]] -= 1
            i += 1
        while freq_t[s[j]] < freq_s[s[j]]:
            freq_s[s[j]] -= 1
            j -= 1
        
        a, b = 0, len(s) - 1

        while freq_t[s[b]] < freq_s[s[b]]:
            freq_s[s[b]] -= 1
            b -= 1
        while freq_t[s[a]] < freq_s[s[a]]:
            freq_s[s[a]] -= 1
            a += 1

        return s[i:j+1] if abs(i-j) < abs(a-b) else s[a:b+1]
