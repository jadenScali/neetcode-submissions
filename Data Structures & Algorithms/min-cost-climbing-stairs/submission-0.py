class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        
        def dfs(n: int):
            if n in cache:
                return cache[n]
            if n <= 1:
                cache[n] = 0
                return cache[n]

            cache[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return cache[n]
        
        return dfs(len(cost))

        