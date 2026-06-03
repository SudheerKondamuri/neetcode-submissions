class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        for i in range(len(nums)) :
            if c[0] != 0 :
                nums[i] = 0
                c[0] -= 1
            elif c[1] !=0 and c[0] == 0 :
                nums[i] = 1
                c[1] -=1
            else :
                nums[i] = 2
                c[2] -=1
                
        