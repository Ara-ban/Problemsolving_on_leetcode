class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            a = (left + right) // 2 
            if arr[a] > arr[a - 1] and arr[a] > arr[a + 1]:
                return a
            if arr[a] < arr[a + 1]:
                left = a + 1
            else:
                right = a - 1  
        return left 
