class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums)==1:
            return(0)
        if nums[0]>nums[1]:
            return(0)
        if nums[-1]>nums[-2]:
            return(len(nums)-1)
        left,right=0,len(nums)-1
        while left<right-1:
            a=(left+right)//2
            if nums[a]> nums[a+1] and  nums[a]> nums[a-1]:
                return(a)
            elif nums[a]< nums[a+1]:
                left=a
            else:
                right=a
