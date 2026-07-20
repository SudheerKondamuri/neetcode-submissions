class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        ans = [nums[0]]
        for j in range(1,len(nums)):
            if nums[j] == nums[j-1]:
                continue
            else :
                ans.append(nums[j])
                i += 1
        nums[:] = ans.copy()
        print(ans)
        return len(ans)


        