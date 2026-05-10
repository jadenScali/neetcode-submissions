class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            curr = nums[i]           
            if curr in diff:
                return [diff[curr], i]

            diff[target - curr] = i

        return [-1,-1]

                