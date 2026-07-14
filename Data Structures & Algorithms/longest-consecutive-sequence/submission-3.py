class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_s = set(nums)
        ans = 0
        for n in n_s:
            if n - 1 not in n_s :
                temp = 1
                i = n
                while i + 1 in n_s :
                    temp += 1
                    i += 1
                ans = max(ans,temp)
        return ans

            

        