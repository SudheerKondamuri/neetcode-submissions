# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n  # The number range is 1 to n
        
        while l <= r:
            mid = l + (r - l) // 2
            res = guess(mid)  # Call API once and store the result
            
            if res == 1:    # Your guess is lower than the picked number
                l = mid + 1
            elif res == -1:  # Your guess is higher than the picked number
                r = mid - 1
            else:            # res == 0 (Correct guess!)
                return mid
                
        return -1
