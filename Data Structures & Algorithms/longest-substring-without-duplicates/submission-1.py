class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, e = 0, 1
        longest = 0
        n = len(s)

        while e < n:
            if s[e] in s[i:e]:
                if i == e:
                    e += 1
                else:
                    i += 1
            else:
                longest = max(longest, e - i)
                e += 1

        return longest + 1
            