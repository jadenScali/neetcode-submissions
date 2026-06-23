class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0

        seen = set()
        for l in s:
            if l in seen:
                longest = max(count, longest)
                count = 1
                seen = set()
                seen.add(l)
            else:
                count += 1
                seen.add(l)
        
        return max(count, longest)
            