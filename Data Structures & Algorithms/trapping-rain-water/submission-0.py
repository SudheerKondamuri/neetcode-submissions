class Solution:
    def trap(self, nums: List[int]) -> int:
        l , r , = 0 , len(nums) - 1
        maxl ,  maxr = nums[0] ,  nums[r]
        ans = 0
        while l < r:
            if maxl <= maxr:
                l += 1
                maxl = max(maxl,nums[l])
                ans += maxl - nums[l]
            else :
                r -= 1
                maxr = max(maxr,nums[r])
                ans += maxr - nums[r]
        return ans

        