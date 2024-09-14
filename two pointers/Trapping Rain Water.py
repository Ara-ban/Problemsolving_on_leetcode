from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left,max_right=[],[]
        left_max,right_max=0,0
        for i in range (n):
            max_left.append(left_max)
            if height[i]>left_max:
                left_max=height[i]
            max_right.append(right_max)
            if height[n-1-i]>right_max:
                right_max=height[n-1-i]
        output=0
        for i in range (n):
            output+=max(0,min(max_right[n-1-i],max_left[i])-height[i])
        return output