from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = -(nums[i] + nums[j])
                if k in seen:
                    # FIX 1: Sort them and use a tuple so the set can store it 
                    # and automatically filter out different orderings!
                    triplet = tuple(sorted([nums[i], nums[j], nums[seen[k]]]))
                    ans.add(triplet)
            seen[nums[i]] = i
            
        # FIX 2: Convert the set of tuples back to a list of lists
        return [list(t) for t in ans]
