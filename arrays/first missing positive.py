class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): 
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n
#to avoid using extra space, we use the table itself for hashing, the solution is also o(n) in terms of speed
