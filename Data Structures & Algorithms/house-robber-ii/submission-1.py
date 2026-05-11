class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_line(nums[:-1]), self.rob_line(nums[1:]))
    
    def rob_line(self, nums: list[int]):
        memo = {}

        def dfs(n: int):

            result = 0
            if n in memo:
                return memo[n]

            if n == 0:
                memo[n] = nums[n]
            elif n == 1:
                memo[n] = max(nums[0], nums[1])
            else:
                memo[n] = max(dfs(n-1), dfs(n-2) + nums[n])
            
            return memo[n]
        
        return dfs(len(nums)-1)





        