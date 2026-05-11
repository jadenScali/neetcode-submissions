class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})

    def helper(self, n, mem):
        if n in mem:
            return mem[n]

        if n <= 2:
            mem[n] = n
            return n

        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        mem[n] = result
        return result
        