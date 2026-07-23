class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        res , i , j = 0 , 0 , len(nums) - 1
        while i <= j:
            remain = limit - nums[j]
            j -= 1
            res += 1
            if i <= j and remain >= nums[i]:
                i += 1
        return res
        