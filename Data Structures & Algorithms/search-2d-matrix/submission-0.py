class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        l =  len(nums)-1
        i , j = 0 , l
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid][-1] < target :
                i = mid+1
            elif nums[mid][-1] > target:
                j = mid-1
            else :
                return True
        if i >= len(nums):
            return False
        l = i
        i , j = 0 , len(nums[0])
        while i <= j:
            mid = i + (j-i)//2
            if nums[l][mid] < target:
                i = mid+1
            elif nums[l][mid] > target:
                j = mid -1
            else :
                return True
        return False