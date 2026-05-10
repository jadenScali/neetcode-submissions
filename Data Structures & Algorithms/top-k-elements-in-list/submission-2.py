class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sums = [[] for _ in range(len(nums))]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, value in freq.items():
            sums[value-1].append(key)

        top_k = []
        i = 0
        while len(top_k) < k:
            curr = len(nums)-1-i

            if len(sums[curr]) == 0:
                i += 1
            else:
                top = sums[curr].pop()
                top_k.append(top)
        
        return top_k