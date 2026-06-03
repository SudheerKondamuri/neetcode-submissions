from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, arr, lo, hi):
        if lo < hi:
            pivot_idx = self.partition(arr, lo, hi)
            self.quicksort(arr, lo, pivot_idx - 1)
            self.quicksort(arr, pivot_idx + 1, hi)

    def partition(self, arr, lo, hi):
        # Random pivot prevents O(n²) on sorted/repeated inputs
        rand = random.randint(lo, hi)
        arr[rand], arr[hi] = arr[hi], arr[rand]

        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        return i + 1