class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})

    def helper(self, n, mem):
        if n in mem:
            return mem[n]

        if n <= 2:
            mem[n] = n
            return n

        result = self.helper(n-1, mem) + self.helper(n-2, mem)
        mem[n] = result
        return result
        