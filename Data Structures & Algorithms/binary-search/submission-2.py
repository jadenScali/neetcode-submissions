class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_i = len(nums) // 2
        runs = 0

        while nums[mid_i] != target:
            runs += 1

            if nums[mid_i] < target:
                mid_i //= 2
            else:
                mid_i = mid_i + ((len(nums) - mid_i) // 2)
            
            if runs >= math.log(len(nums), 10) + 1:
                return -1
        
        return mid_i
        