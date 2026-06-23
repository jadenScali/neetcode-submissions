class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        v = {}

        for n in nums:
            if n not in v:
                v[n] = 1
        
        possible_starts = []

        for key in v:
            if key-1 not in v:
                possible_starts.append(key)
        
        big = 0
        for num in possible_starts:
            count = 0
            while num in v:
                num += 1
                count += 1
            if count > big:
                big = count
        
        return big
        