class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triples = []

        for i, n in enumerate(nums):
            target = -n

            potential = nums[:i] + nums[i+1:]
            matches = self.twoSum(potential, target)
            for match in matches:
                triple = [n, match[0], match[1]]
                triple.sort()
                if triple not in triples:
                    triples.append(triple)
        
        return triples
                

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:

        mem = {}
        pairs = []

        for i, n in enumerate(nums):
            if n in mem:
                pair = [mem[n], n]
                pair.sort()
                if pair not in pairs:
                    pairs.append(pair)

            mem[target - n] = n
        
        return pairs


        


        