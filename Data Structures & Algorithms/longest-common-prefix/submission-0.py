class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(min(strs,key=len))) :
            t = strs[0][i]
            for j in range(len(strs)) :
                if strs[j][i] != t:
                    return ans
            
            ans += t
        return ans
                

        