class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i = 0
        n = min(len(w1), len(w2))
        ans = ""
        
        # 1. Loop merges the alternating characters up to the shorter string's length
        while i < n:
            ans += w1[i]
            ans += w2[i]
            i += 1
            
        # 2. Append whatever is left over from the longer string
        ans += w1[i:]
        ans += w2[i:]
        
        return ans
