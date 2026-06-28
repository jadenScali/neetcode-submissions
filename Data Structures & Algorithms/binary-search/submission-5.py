class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_2(nums, target, 0, len(nums)-1)
        
    def search_2(self, nums, target, start, end):
        if start > end:
            return -1
        
        mid = start + ((end - start) // 2)

        if target < nums[mid]:
            return self.search_2(nums, target, start, mid - 1)
        elif target > nums[mid]:
            return self.search_2(nums, target, mid + 1, end)
        else:
            return mid