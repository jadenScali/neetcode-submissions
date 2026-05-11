class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(n: int):
            if n in memo:
                return memo[n]

            if n == 0:
                memo[n] = nums[n]
            elif n == 1:
                memo[n] = max(nums[0], nums[1])
            else:
                memo[n] = max(dfs(n-2) + nums[n], dfs(n-1))

            return memo[n]
        
        return dfs(len(nums)-1)
        