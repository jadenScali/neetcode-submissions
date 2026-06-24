class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        s = 0
        h = height

        while h[s] == 0:
            s += 1

        while s < n:
            e = s + 1
            t = e

            while e < n:
                if h[e] >= h[s]:
                    t = e
                    break
                elif h[e] > h[t]:
                    t = e
                
                e += 1
            
            total += self.get_vol(s, t, height)
            s = e

        return total
    
    def get_vol(self, s, e, h):
        x = e - s - 1
        y = min(h[s], h[e])
        vol = x*y

        for i in range(s+1, e):
            vol -= min(h[i], y)
        
        return vol


        