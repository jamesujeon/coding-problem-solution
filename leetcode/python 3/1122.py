# 문제 링크: https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=lambda x: (x not in arr2, arr2.index(x) if x in arr2 else x))