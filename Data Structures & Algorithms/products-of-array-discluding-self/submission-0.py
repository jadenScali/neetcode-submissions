class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        total_product = 1
        nums_zeros = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
            else:
                nums_zeros += 1

        
        for i in range(len(nums)):
            if nums_zeros >= 2:
                r.append(0)
            elif nums_zeros == 1:
                if nums[i] == 0:
                    r.append(total_product)
                else:
                    r.append(0)
            else:
                r.append(total_product//nums[i])
        
        return r
        