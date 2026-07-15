class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        for n in nums:
            if n in hm:
                hm[n] += 1
            else :
                hm[n] = 1
        threshold = len(nums) // 3
        
        ans = [key for key, count in hm.items() if count > threshold]
        return ans
        