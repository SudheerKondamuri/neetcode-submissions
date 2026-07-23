from typing import List

class Solution:     
    def maxArea(self, nums: List[int]) -> int:         
        ans = 0         
        i , j = 0 , len(nums)-1         
        while i < j:             
            curr = self.carea(nums, i, j)             
            if nums[i] <= nums[j]:
                i += 1
            else :
                j -= 1
            ans = max(ans, curr)         
        return ans     

    def carea(self, nums, i, j):         
        return min(nums[i], nums[j]) * (j - i)
