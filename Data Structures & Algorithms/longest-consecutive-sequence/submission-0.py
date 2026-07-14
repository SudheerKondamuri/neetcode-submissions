class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1 if n>=1 else 0
        for i in range(n):
            temp = 1
            if (nums[i] + 1) in nums :
                temp += 1
                r = 2
                while(True):
                    if (nums[i]+r) in nums :
                        temp += 1
                        r += 1
                    else :
                        break
            ans = max(temp,ans)
        return ans

            

        