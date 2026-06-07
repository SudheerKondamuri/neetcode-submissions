class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f_i = [item for item , count in c.most_common(k)]
        return f_i
        
        