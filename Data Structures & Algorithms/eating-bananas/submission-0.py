import math
from typing import List


class Solution:

    def minEatingSpeed(self, nums: List[int], h: int) -> int:

        def cal(nums, k, h):
            ans = 0
            for i in range(len(nums)):
                ans += math.ceil(nums[i] / k)
            # Return True if Koko finishes within h hours, False otherwise
            return ans <= h

        # Start l at 1 to prevent dividing by 0
        l, r = 1, max(nums)

        while l <= r:
            mid = l + (r - l) // 2
            if cal(nums, mid, h):
                r = mid - 1  # Speed works! Let's try to find a smaller speed
            else:
                l = mid + 1  # Too slow! We must speed Koko up

        return l
