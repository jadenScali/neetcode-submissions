class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        for i in range(len(nums) - k + 1):
            window_max = nums[i]
            for j in range(i+1, i + k):
                window_max = max(window_max, nums[j])
            
            ans.append(window_max)
        
        return ans

        