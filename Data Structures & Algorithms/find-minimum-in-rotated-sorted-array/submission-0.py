class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            if r - l <= 1:
                return min(nums[l], nums[r])
                
            m = (l+r) // 2

            if nums[l] < nums[r]:
                return nums[l]

            if nums[l] < nums[m]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m

        return -1

        