class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = piles[0]

        for p in piles:
            if p > r:
                r = p;

        last_valid = r

        while l <= r:
            mid = (l + r) // 2

            if self.h(piles, mid) <= h:
                last_valid = mid
                r = mid - 1
            else:
                l = mid + 1

        return last_valid


    
    def h(self, piles: List[int], k: int) -> int:
        time = 0

        for p in piles:
            time += (p // k) + 1

        return time

        