class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] *= -1
#the solution uses the fact that the only case of nums that you will visit more than once is the one indexed by duplicate
