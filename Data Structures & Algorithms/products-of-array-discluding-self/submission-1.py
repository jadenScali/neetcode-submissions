class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = {}

        curr_prod = 1
        for i, n in enumerate(nums):
            before[i] = curr_prod
            curr_prod *= n
        
        curr_prod = 1
        final = [1]*len(nums)
        for i in range(len(nums) -1, -1, -1):
            final[i] = curr_prod * before[i]
            curr_prod *= nums[i]
        
        return final
        