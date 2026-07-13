class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        
        # Step 1: Calculate prefix products
        prefix = 1
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products and multiply on the fly
        suffix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
